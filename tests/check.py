#!/usr/bin/env python3
"""Check that the vocabulary, the context, the examples and the queries agree.

1. Every term the context names is defined in vocab/decision.ttl, and every term defined there is in the context.
2. Every example parses with the context of this repository, uses only defined terms, and takes each listed value
   from the list of its property.
3. In every example the nature matches the number of options put (none, one, two or more), the recommended and the
   chosen options are among the options put, and a refused or deferred decision retains no option.
4. The three queries give the answers the README states, and the negative control finds what it must.

Needs rdflib (7 or later). Exit code 0 when everything passes, 1 otherwise."""
import json
import pathlib
import sys

from rdflib import Graph, Namespace, RDF, URIRef
from rdflib.namespace import SKOS

ROOT = pathlib.Path(__file__).resolve().parent.parent
DEC = Namespace("https://w3id.org/decision#")
CONTEXT_IRI = "https://w3id.org/decision/context.jsonld"
SCHEME_OF = {
    DEC.nature: DEC.NatureScheme,
    DEC.reversibility: DEC.ReversibilityScheme,
    DEC.factualBasis: DEC.FactualBasisScheme,
    DEC.requiredOversight: DEC.OversightScheme,
    DEC.outcome: DEC.OutcomeScheme,
    DEC.urgency: DEC.UrgencyScheme,
    DEC.recommendationShown: DEC.RecommendationShownScheme,
    DEC.execution: DEC.ExecutionScheme,
}
NO_OPTION_RETAINED = (DEC.Refused, DEC.Deferred, DEC.Escalated)
FAST_SECONDS = 30
SCHEMES = set(SCHEME_OF.values())


def load_vocab():
    g = Graph()
    g.parse(ROOT / "vocab" / "decision.ttl", format="turtle")
    return g


def defined_terms(vocab):
    return {s for s in vocab.subjects() if isinstance(s, URIRef) and str(s).startswith(str(DEC))}


def local_context():
    return json.loads((ROOT / "context" / "decision.context.jsonld").read_text(encoding="utf-8"))["@context"]


def load_example(path, context):
    """Parse an example with the context of this repository in place of its published address."""
    doc = json.loads(path.read_text(encoding="utf-8"))
    ctx = doc["@context"]
    if ctx == CONTEXT_IRI:
        doc["@context"] = context
    else:
        doc["@context"] = [context if c == CONTEXT_IRI else c for c in ctx]
    g = Graph()
    g.parse(data=json.dumps(doc), format="json-ld")
    return g


def check_context(vocab, context, bad):
    terms = defined_terms(vocab)
    named = set()
    for key, value in context.items():
        target = value.get("@id") if isinstance(value, dict) else value
        if isinstance(target, str) and target.startswith("dec:") and len(target) > 4:
            named.add(DEC[target[4:]])
    for term in sorted(named - terms):
        bad.append(f"the context names {term}, which the vocabulary does not define")
    for term in sorted(terms - named - SCHEMES):
        bad.append(f"the vocabulary defines {term}, which the context does not name")
    return terms


def check_example(name, g, vocab, terms, bad):
    for s, p, o in g:
        for node in (p, o):
            if isinstance(node, URIRef) and str(node).startswith(str(DEC)) and node not in terms:
                bad.append(f"{name}: {node} is not defined in the vocabulary")
        if p in SCHEME_OF and (o, SKOS.inScheme, SCHEME_OF[p]) not in vocab:
            bad.append(f"{name}: {o} is not a value of {p}")
    decisions = sorted(g.subjects(RDF.type, DEC.Decision))
    if not decisions:
        bad.append(f"{name}: no decision found")
    for d in decisions:
        options = set(g.objects(d, DEC.option))
        nature = g.value(d, DEC.nature)
        expected = DEC.Alert if len(options) == 0 else DEC.Validation if len(options) == 1 else DEC.Arbitration
        if nature is not None and nature != expected:
            bad.append(f"{name}: {d} has {len(options)} option(s) and nature {nature}")
        for prop in (DEC.recommendedOption, DEC.chosenOption):
            for o in g.objects(d, prop):
                if o not in options:
                    bad.append(f"{name}: {d} {prop} is not among the options put")
        outcome = g.value(d, DEC.outcome)
        if outcome in NO_OPTION_RETAINED and g.value(d, DEC.chosenOption) is not None:
            bad.append(f"{name}: {d} is refused, deferred or escalated and retains an option")
        if g.value(d, DEC.execution) is not None and outcome not in (DEC.Approved, DEC.Amended):
            bad.append(f"{name}: {d} carries an execution although it was not approved")
        put, decided = g.value(d, DEC.putAt), g.value(d, DEC.decidedAt)
        if put is not None and decided is not None and decided.toPython() < put.toPython():
            bad.append(f"{name}: {d} was decided before it was put")
        if decided is not None and outcome is None:
            bad.append(f"{name}: {d} has a decision time and no outcome")
    return decisions


def seconds_taken(g, query_file):
    """Time between putAt and decidedAt for each row of a query that returns ?decision ?putAt ?decidedAt."""
    text = (ROOT / "queries" / query_file).read_text(encoding="utf-8")
    return {str(row[0]): (row[2].toPython() - row[1].toPython()).total_seconds() for row in g.query(text)}


def run(g, query_file):
    text = (ROOT / "queries" / query_file).read_text(encoding="utf-8")
    return [tuple(str(v) for v in row) for row in g.query(text)]


def main():
    bad = []
    vocab = load_vocab()
    context = local_context()
    terms = check_context(vocab, context, bad)

    everything = Graph()
    count = 0
    for path in sorted((ROOT / "examples").glob("*.jsonld")):
        g = load_example(path, context)
        count += len(check_example(path.name, g, vocab, terms, bad))
        everything += g

    low = run(everything, "irreversible-below-signature.rq")
    if low != [("urn:example:decision:quotes-0912", str(DEC.Confirmation))]:
        bad.append(f"irreversible-below-signature.rq: unexpected answer {low}")
    not_followed = [row[0] for row in run(everything, "recommendation-not-followed.rq")]
    if not_followed != ["urn:example:decision:payment-7730:2", "urn:example:decision:quotes-0912"]:
        bad.append(f"recommendation-not-followed.rq: unexpected answer {not_followed}")
    if run(everything, "classified-without-policy.rq"):
        bad.append("classified-without-policy.rq: finds a decision although every example names its policy")

    control = Graph()
    for triple in everything:
        if triple[1] != DEC.classifiedUnder:
            control.add(triple)
    found = len(run(control, "classified-without-policy.rq"))
    if found != count:
        bad.append(f"negative control: {found} of {count} decisions found once the policy is dropped")

    # Queries added in 0.2.0
    taken = seconds_taken(everything, "irreversible-times.rq")
    fast = sorted(d for d, s in taken.items() if s < FAST_SECONDS)
    if fast != ["urn:example:decision:quotes-0912"]:
        bad.append(f"irreversible-times.rq: decided in under {FAST_SECONDS} s: {fast}")
    late = run(everything, "late-in-session.rq")
    if [row[0] for row in late] != ["urn:example:decision:quotes-0912"]:
        bad.append(f"late-in-session.rq: unexpected answer {late}")
    undone = run(everything, "undone-then-replaced.rq")
    if undone != [("urn:example:decision:site-fix:1", "urn:example:decision:site-fix:2")]:
        bad.append(f"undone-then-replaced.rq: unexpected answer {undone}")
    waiting = run(everything, "open-dependencies.rq")
    if waiting != [("urn:example:decision:invoice-7730:close", "urn:example:decision:payment-7730:2", str(DEC.Approved))]:
        bad.append(f"open-dependencies.rq: unexpected answer {waiting}")

    result = {
        "terms_defined": len(terms - SCHEMES),
        "decisions_in_examples": count,
        "triples": len(everything),
        "irreversible_below_signature": [row[0] for row in low],
        "recommendation_not_followed": not_followed,
        "negative_control_finds": found,
        "irreversible_decided_in_under_30_s": fast,
        "late_in_session": [row[0] for row in late],
        "undone_then_replaced": [list(row) for row in undone],
        "waiting_for_another_decision": [row[0] for row in waiting],
    }
    print(json.dumps(result, indent=1))
    print("PASS: the vocabulary, the context, the examples and the queries agree." if not bad else
          "FAIL:\n- " + "\n- ".join(bad))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
