# decision

A small vocabulary for the characteristics of a decision put to a person: what kind of choice it was, what was at
stake, how much oversight it required, and how it ended. Version 0.1.0, 13 November 2026. Author: Laurent Lemonnier.

**This is a vocabulary, not a standard.** One author wrote it; nobody else uses it yet. Its namespace is
`https://w3id.org/decision#` (prefix `dec:`). It is not part of the Decision Provenance Standard and is not endorsed
by its Steward.

## Why

Records of decisions describe the decision itself in free text, or with a class each organisation names as it likes.
Records of what an AI agent did each carry their own table of action types. So two questions that matter cannot be
asked across records: which decisions could not be undone, and how much oversight did they get?

Provenance does not answer them either. Provenance says where something came from: who, when, from what. It does not
say what a decision is. That is why these terms are kept apart from
[decision-prov](https://github.com/Laurent-Lemonnier/decision-prov), which reads decision records as W3C PROV and whose
terms only name the members of those records.

## The terms

Two classes: `dec:Decision` and `dec:Option`. Sixteen properties:

| Property | Says | Criterion |
|---|---|---|
| `dec:whyNow` | why the decision is put now | one or two sentences, as put to the person |
| `dec:option` | an option put to the person | it was on the screen or in the document the person decided from |
| `dec:recommendedOption` | the option the preparer recommended | one of the options put |
| `dec:chosenOption` | the option the person retained | absent when refused or deferred |
| `dec:deadline` | when the decision loses its object | stated in what was put; absent otherwise |
| `dec:nature` | Alert, Validation or Arbitration | no option put, one, two or more |
| `dec:reversibility` | Reversible, Compensable or Irreversible | what the policy declares for the operation; the least reversible of several |
| `dec:magnitude` | a number and a unit | stated in the proposal; absence is not zero |
| `dec:affectsThirdParty` | true or false | the action reaches someone outside the decider's organisation |
| `dec:legalEffect` | true or false | the action creates, changes or ends a right or an obligation of a person, or similarly significantly affects that person |
| `dec:factualBasis` | SourcesRead, SourcesCited or Unsourced | every fact sourced and read for this decision; sourced; at least one fact unsourced |
| `dec:requiredOversight` | NoApproval, Confirmation or Signature | the least a person had to do before the action could proceed |
| `dec:outcome` | Approved, Amended, Refused or Deferred | what the person decided; absent while open |
| `dec:classifiedUnder` | the policy, with its version, that assigned the classification | an IRI or a published identifier |
| `dec:classifiedBy` | who or what applied that policy | a person, or a named system applying declared rules |
| `dec:recordedIn` | a document that records the decision | an IRI, or a digest of its bytes |

The definitions are in [vocab/decision.ttl](vocab/decision.ttl) (RDFS and SKOS) and repeated in [vocab.md](vocab.md).
The JSON-LD 1.1 context is [context/decision.context.jsonld](context/decision.context.jsonld), also at
`https://w3id.org/decision/context.jsonld`.

Two rules hold the rest together. A classification names the policy that assigned it (`dec:classifiedUnder`): without
one it is an opinion. And a value that was not recorded is left out: absence never means "none" or "zero".

## Examples

[examples](examples) holds four invented documents, five decisions:

- `refund-validation.jsonld`: one proposal, a refund of 120.00 EUR, approved under a signature;
- `maintenance-reapproval.jsonld`: a fix approved, run, rolled back after a failed check, then approved again as a new
  decision that replaces the first (modelled on a real case, every name removed);
- `quote-arbitration.jsonld`: three quotes, one recommended, another retained;
- `certificate-alert.jsonld`: a signal with no proposal, set aside.

The three queries in [queries](queries) answer, on those five decisions:

- `irreversible-below-signature.rq`: one decision cannot be undone, reaches a third party and went through on a
  confirmation only (the quotes);
- `recommendation-not-followed.rq`: one decision retained another option than the one recommended (the quotes);
- `classified-without-policy.rq`: none; and with every `dec:classifiedUnder` dropped, all five (the negative control).

## Tried on real decisions

The terms were tried on 18 decisions recorded in the author's organisation on 12 and 13 November 2026 (requests from
clients, prepared by a system, approved by a person; 23 approvals signed with a passkey). Those records are not
published. From what they hold:

| Could be assigned | Decisions |
|---|---|
| nature, required oversight, why now, options | 18 of 18 |
| factual basis (sourced or not; "read" and "cited" could not be told apart) | 16 of 18 |
| outcome ("approved" and "amended" could not be told apart) | 14 of 18 |
| affects a third party | 13 of 18 |
| reversibility | 8 of 18 |
| magnitude, legal effect, deadline | 0 of 18 |

Reversibility failed on ten decisions because their plans used operations the organisation's scale does not list.
Magnitude, legal effect and deadline were never recorded, and the policy version was written into the signed
specification only from 13 November. So the trial says as much about what a system must record as about the terms:
three properties could not be filled at all, and reversibility for fewer than half of the decisions, from records
that were not written with these terms in mind.

## What it does not cover

- The conditions in which the person decided: what was shown, in what order, for how long. Not in this version.
- Relations between decisions. The second example uses `dcterms:replaces`; this vocabulary adds no term of its own.
- Who was entitled to decide, and whether the approval is authentic. That is the work of a record format and its
  verifier, for example the Decision Provenance Standard with its action binding and signatures.
- The logic of a rule-based decision, which DMN (Object Management Group) describes.

## Earlier work

The W3C Decisions and Decision-Making Incubator Group published "Towards a Semantic Decision Representation Format"
in 2012. Its sample decision ontology says of itself that it is "not a proposal for a standard ontology, merely an
illustration", and the report recommended a working group. DecPROV (Nicholas Car) later aligned that ontology with
PROV-O, to record decisions already made, and added an agent. Their terms describe the question, the making of the
decision and the solution accepted. The pages of both name no term for reversibility, effect on a third party, legal
effect or required oversight, which are what this vocabulary adds. Their ontology files were not read term by term.

## Run

```
pip install rdflib
python3 tests/check.py
```

The check passes when every term of the context is defined, every example uses only defined terms and listed values,
the nature of each decision matches the number of options put, and the queries answer as stated above.

## Licence

Code (`tests`, `queries`): Apache-2.0 ([LICENSE](LICENSE)). Text, the context and the vocabulary (`README.md`,
`vocab.md`, `vocab/`, `context/`): CC-BY 4.0 ([LICENSE-CC-BY-4.0](LICENSE-CC-BY-4.0)). The data in the examples is
invented. Cite as in [CITATION.cff](CITATION.cff).

"Decision Provenance Standard" is a trademark of Etsion Brands Ltd., used here to identify the Standard.
