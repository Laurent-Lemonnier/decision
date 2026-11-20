# decision

A small vocabulary for the characteristics of a decision put to a person: what kind of choice it was, what was at
stake, how much oversight it required, in what conditions the person decided, and what became of it. Version 0.2.0, 14 November 2026. Author: Laurent Lemonnier.

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

Two classes, `dec:Decision` and `dec:Option`, and thirty-three properties in five groups. Only the first group is the
core; the four others were added in 0.2.0 and are optional.

**Core** (0.1.0, unchanged)

| Property | Says | Criterion |
|---|---|---|
| `dec:whyNow` | why the decision is put now | one or two sentences, as put to the person |
| `dec:option` | an option put to the person | it was on the screen or in the document the person decided from |
| `dec:recommendedOption` | the option the preparer recommended | one of the options put |
| `dec:chosenOption` | the option the person retained | absent when refused, deferred or escalated |
| `dec:deadline` | when the decision loses its object | stated in what was put; absent otherwise |
| `dec:nature` | Alert, Validation or Arbitration | no option put, one, two or more |
| `dec:reversibility` | Reversible, Compensable or Irreversible | what the policy declares for the operation; the least reversible of several |
| `dec:magnitude` | a number and a unit | stated in the proposal; absence is not zero |
| `dec:affectsThirdParty` | true or false | the action reaches someone outside the decider's organisation |
| `dec:legalEffect` | true or false | the action creates, changes or ends a right or an obligation of a person, or similarly significantly affects that person |
| `dec:factualBasis` | SourcesRead, SourcesCited, Unsourced or SourcesUnavailable | every fact sourced and read for this decision; sourced; at least one fact unsourced; a named source could not be read |
| `dec:requiredOversight` | NoApproval, Confirmation or Signature | the least a person had to do before the action could proceed |
| `dec:outcome` | Approved, Amended, Refused, Deferred or Escalated | what the person decided; absent while open |
| `dec:classifiedUnder` | the policy, with its version, that assigned the classification | an IRI or a published identifier |
| `dec:classifiedBy` | who or what applied that policy | a person, or a named system applying declared rules |
| `dec:recordedIn` | a document that records the decision | an IRI, or a digest of its bytes |

**Who**

| Property | Says | Criterion |
|---|---|---|
| `dec:decider` | the one accountable person | an IRI or a published identifier |
| `dec:preparedBy` | who or what prepared what was put | the author of the options and the recommendation, not of the choice |

**Context**

| Property | Says | Criterion |
|---|---|---|
| `dec:objective` | what the decision is meant to achieve | as stated in what was put |
| `dec:assumption` | something taken as true without a source | stated as an assumption in what was put |
| `dec:statedRisk` | a risk named to the person | it was shown; a risk known and not shown is not stated |
| `dec:contextVersion` | the version of the facts the proposal was built from | an identifier or a digest |
| `dec:shownContent` | what the person decided from, as rendered | an IRI or a digest of the view or the document |

**Conditions** (they describe a person's behaviour: record the least that serves, show it to the person, keep it out of any assessment of the person)

| Property | Says | Criterion |
|---|---|---|
| `dec:putAt` | when the decision was put before the person | shown, or sent when only the sending is known |
| `dec:decidedAt` | when the person gave the outcome | never earlier than `putAt` |
| `dec:rankInSession` | which decision of the session it was | one, plus the confirmations and signatures already given in the same session |
| `dec:sourcesOpened` | how many named sources the person opened | counted by the system; absent when it does not count |
| `dec:urgency` | Immediate, SameDay or Planned | the band the policy assigns |
| `dec:recommendationShown` | BeforeChoice, AfterChoice or NotShown | whether the recommendation was visible when the person began to choose |

**Follow-up**

| Property | Says | Criterion |
|---|---|---|
| `dec:successCriterion` | how success will be judged | stated before the action is taken |
| `dec:execution` | NotStarted, CarriedOut, Failed or Undone | from the record of the action; only for an approved or amended decision |
| `dec:reviewTrigger` | when the decision is to be put again | a date, an event, a threshold |
| `dec:dependsOn` | a decision that must be decided first | names the other decision |

The definitions are in [vocab/decision.ttl](vocab/decision.ttl) (RDFS and SKOS) and repeated in [vocab.md](vocab.md).
The JSON-LD 1.1 context is [context/decision.context.jsonld](context/decision.context.jsonld), also at
`https://w3id.org/decision/context.jsonld`.

Two rules hold the rest together. A classification names the policy that assigned it (`dec:classifiedUnder`): without
one it is an opinion. And a value that was not recorded is left out: absence never means "none" or "zero".

## Where the 0.2.0 terms come from

The added terms were drawn from two sides and set against each other: an interface for deciding that the author's
organisation specified in 2025 and 2026 (its data model, and the table mapping that model to the screen), and
published work. Where one side is silent, the table says so.

| In the interface specification | In published work | Term |
|---|---|---|
| a context snapshot per decision: objective, risks, assumptions, with a version that can be compared | the Decision Provenance Standard's record: assumptions depended on, context at decision | `objective`, `assumption`, `statedRisk`, `contextVersion` |
| "a critical action does not leave with a stale version"; the prepared action shows its content, version and digest | W3C Secure Payment Confirmation: what is displayed is what is signed | `shownContent`, `contextVersion` |
| a queue in three bands (now, today, to prepare), ordered by a deterministic rule | interruption research: a task boundary is a less costly moment than the middle of a task (Iqbal and Bailey, CHI 2008; Fischer et al., MobileHCI 2011) | `urgency` |
| every action shown says "why now"; one recommended action, two others at most | Buçinca, Malaya and Gajos (CSCW 2021): making a person commit before seeing the system's answer reduces over-reliance | `recommendationShown` |
| silent on counting; it only limits what is shown at once (eight situations per page) and refuses, in writing, infinite scrolling and artificial reward | Regulation (EU) 2024/1689, Article 14(4)(b): remain aware of automation bias; practitioners' accounts of approval fatigue (time to approve falling, approval rate rising) | `putAt`, `decidedAt`, `rankInSession`, `sourcesOpened` |
| sources shown as "none", "not synchronised", "access withdrawn" or "deleted", never as absent | nothing found | value `SourcesUnavailable` |
| the action's state (to do, doing, done, blocked), its receipt, its log | the Standard's success criteria and re-decision trigger | `successCriterion`, `execution`, `reviewTrigger` |
| a dependency between decisions ("blocked by"); a validation that says "validated by" | the Standard's accountable owner, drafting authority and related decisions | `dependsOn`, `decider`, `preparedBy`, value `Escalated` |

## Examples

[examples](examples) holds six invented documents, nine decisions:

- `refund-validation.jsonld`: one proposal, a refund of 120.00 EUR, approved under a signature and carried out;
- `maintenance-reapproval.jsonld`: a fix approved, run, undone after a failed check, then approved again as a new
  decision that replaces the first (modelled on a real case, every name removed);
- `quote-arbitration.jsonld`: three quotes, one recommended, another retained in eight seconds, ninth decision of the
  session;
- `certificate-alert.jsonld`: a signal with no proposal, set aside;
- `payment-escalation.jsonld`: a payment passed to someone with more authority because a source could not be read,
  decided there after the person committed before seeing the recommendation, and a third decision that waits for it;
- `recorded-refund.jsonld`: a refund whose record is public and named by the digest of its bytes (see the next
  section).

The queries in [queries](queries) answer, on those nine decisions:

- `irreversible-below-signature.rq`: one decision cannot be undone, reaches a third party and went through on a
  confirmation only (the quotes);
- `recommendation-not-followed.rq`: two decisions retained another option than the one recommended;
- `classified-without-policy.rq`: none; and with every `dec:classifiedUnder` dropped, all nine (the negative control);
- `irreversible-times.rq`: when each irreversible decision was put and decided; computed from it, one was decided in
  under thirty seconds (the quotes);
- `late-in-session.rq`: one decision came eighth or later in its session (the quotes);
- `undone-then-replaced.rq`: one action was undone and its decision replaced (the fix);
- `open-dependencies.rq`: one decision waits for another, which is approved.

That the same decision answers four of the queries is the point of the example: irreversible, on a confirmation,
in eight seconds, late in the session.

## One decision described here and recorded elsewhere

`recorded-refund.jsonld` describes a decision whose record is public: the refund of the `one-chain` case in
[dps-scitt-decision-layer](https://github.com/Laurent-Lemonnier/dps-scitt-decision-layer/tree/21cf862c1ed6c70349cf7ad29654b56b839abb46/interop/one-chain),
a synthetic case recorded under the Decision Provenance Standard. `dec:recordedIn` names the record three ways:

- by the SHA-256 of the bytes of `decision-record.json`, written as an RFC 6920 `ni:` URI (in hex,
  `056a7135a4a71cd429177e2c4ad2a51d004fe45872a7cec76f290f92f2e61ace`; `sha256sum` on the file at the pinned commit
  gives it);
- by the address of that file at the pinned commit;
- by the entry, in the transparency log ts.isoluce.net (leaf 0), of the action-binding attachment A1, the one sealed
  at the approval. The log does not hold `decision-record.json` itself, and A1 stops at the outcome: the run is in
  A2, which has its own entry.

Where each value of the example comes from:

| Terms | Source in the record |
|---|---|
| `label`, `whyNow` | `decision_statement`, `context_at_decision` |
| `nature`, `option` | the view the person signed (`review-view.txt`) shows one refund: one option was put. The record's `options_considered` lists three options its drafter weighed; they were not put to the person |
| `magnitude`, `classifiedUnder` | the view: the amount, the policy and its version |
| `requiredOversight`, `outcome`, `decidedAt` | the person's signed approval (`signatures-attachment.json`, stage `o1`) |
| `shownContent` | `shown_view_digest`, which that signature covers |
| `putAt` | the review stage `v1` |
| `decider`, `preparedBy` | the accountable owner; the drafting authority |
| `assumption`, `successCriterion`, `reviewTrigger` | `assumptions_depended_on`, `success_criteria`, `re_decision_trigger` |
| `execution` | the attempt and result stages of the second attachment |
| `reversibility`, `affectsThirdParty`, `legalEffect`, `factualBasis` | no member of the record carries them: they are this example's own classification |
| `recommendedOption`, `chosenOption`, `recommendationShown` | the record has no recommendation member. The proposal is the drafting system's (stage `p1`, 10:00:03), the person's review (`v1`, 10:00:40) shows it, and the approval (`o1`) retains it: so the one option is both recommended and chosen, and shown before the choice. That is this example's reading, not a member of the record |
| the identifiers of the decision and of its option | invented for the example; the record's `decision_id` is `DR-2026-1104` |
| `classifiedBy`, `contextVersion`, `urgency`, `rankInSession`, `sourcesOpened` | not in the record, and left out |

The two do different work. The record and its verifier answer whether the approval is authentic, what exactly was
approved and whether what ran was that. This document says what kind of decision it was, so that it can be queried
with others. Nothing in this repository checks the digest or the signature. The mapping is the author's reading; the
Standard's Steward has not reviewed it.

## Tried on real decisions

The terms were tried on 18 decisions recorded in the author's organisation on 12 and 13 November 2026 (requests from
clients, prepared by a system, approved by a person; 23 approvals signed with a passkey). Those records are not
published. From what they hold:

| Could be assigned | Decisions |
|---|---|
| nature, required oversight, why now, options, decider, prepared by, recommendation shown (always before the choice, by design) | 18 of 18 |
| context version, shown content (digests of the plan and of the view) | 17 of 18 |
| factual basis (sourced or not; "read" and "cited" could not be told apart) | 16 of 18 |
| outcome ("approved" and "amended" could not be told apart) | 14 of 18 |
| put at and decided at (the request for a signature and the signature) | 13 of 18 |
| affects a third party | 13 of 18 |
| execution | 12 of 18 |
| success criterion (the plan carries a check) | 11 of 18 |
| reversibility | 8 of 18 |
| magnitude, legal effect, deadline, objective, assumption, urgency, rank in session, sources opened, review trigger, depends on | 0 of 18 |

Reversibility failed on ten decisions because their plans used operations the organisation's scale does not list.
Ten properties were never recorded as such; stated risks could not be told from the records; and the policy version
was written into the signed specification only from 13 November. So the trial says as much about what a system must record as about the terms.

## What it does not cover

- Whether a decision was a good one, or whether the person understood it. The conditions group records what a
  system can count; it measures neither attention nor judgement.
- Replacement of one decision by another: the examples use `dcterms:replaces`.
- Who was entitled to decide, and whether the approval is authentic. That is the work of a record format and its
  verifier, for example the Decision Provenance Standard with its action binding and signatures.
- The logic of a rule-based decision, which DMN (Object Management Group) describes.

## Earlier work

The W3C Decisions and Decision-Making Incubator Group published "Towards a Semantic Decision Representation Format"
in 2012. Its sample decision ontology says of itself that it is "not a proposal for a standard ontology, merely an
illustration", and the report recommended a working group. DecPROV (Nicholas Car) later aligned that ontology with
PROV-O, to record decisions already made, and added an agent. Their terms describe the question, the making of the
decision and the solution accepted. The pages of both name no term for reversibility, effect on a third party, legal
effect or required oversight, which are what this vocabulary adds. The Decision Ontology file was not read term by term.
DecPROV 2.0 was later read in full: [alignments/decprov.md](alignments/decprov.md) says where each term here would sit
in it. That table is the author's reading; nothing in this repository asserts an equivalence.

## Versions

- 0.1.0, 13 November 2026: the core, sixteen properties.
- 0.2.0, 14 November 2026: seventeen properties in four optional groups (who, context, conditions, follow-up), two
  values (`Escalated`, `SourcesUnavailable`), three lists (urgency, recommendation shown, execution), one example,
  four queries. No 0.1.0 term was removed or renamed; `chosenOption`, `factualBasis` and `outcome` take the new values
  into account.
- 14 November 2026, still 0.2.0: one example added, `recorded-refund.jsonld`, that names a public record by the
  digest of its bytes. No term added or changed.

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
