# Vocabulary: `https://w3id.org/decision#`

Prefix `dec:`. Version 0.1.0. This page is written from [vocab/decision.ttl](vocab/decision.ttl), which governs.

## Classes

| Term | Definition |
|---|---|
| `dec:Decision` | A choice put to one accountable person, or made by that person, about whether and how an action is taken. One Decision has at most one outcome. |
| `dec:Option` | A course of action put to the person in a Decision. |

## Properties

| Term | Definition |
|---|---|
| `dec:affectsThirdParty` | True when the action, once taken, reaches a person or an organisation outside the decider's own: a message sent to them, a payment, a publication, a change to their data or their contract. |
| `dec:chosenOption` | The option the person retained. Absent when the outcome is Refused or Deferred. |
| `dec:classifiedBy` | Who or what applied the policy: a person, or a named system applying declared rules. |
| `dec:classifiedUnder` | The policy, with its version, under which nature, reversibility and required oversight were assigned: an IRI, or an identifier the organisation publishes. A classification with no policy named is an opinion. |
| `dec:deadline` | The time after which the decision has no object, or after which a stated consequence follows. Absent when none was stated: absence is not 'no deadline'. |
| `dec:factualBasis` | How the facts the proposal relies on were sourced when the decision was put. |
| `dec:legalEffect` | True when the action creates, changes or ends a right or an obligation of a person, or similarly significantly affects that person. |
| `dec:magnitude` | The size of what is decided, as a number and a unit stated in the proposal (an amount and a currency, a number of people, a number of files). Absent when the proposal states none: absence is not zero. |
| `dec:nature` | What kind of choice was put, by the number of options put: none (Alert), one (Validation), two or more (Arbitration). |
| `dec:option` | An option put to the person. Criterion: it was on the screen or in the document the person decided from. |
| `dec:outcome` | What the person decided. Absent while the decision is open. |
| `dec:recommendedOption` | The option whoever prepared the decision recommended, when one was recommended. It is one of the options put. |
| `dec:recordedIn` | A document that records this decision, named by an IRI or by a digest of its bytes. This vocabulary does not say what the record must contain, nor how it is verified. |
| `dec:requiredOversight` | The least a person had to do, under the policy named by classifiedUnder, before the action could proceed. |
| `dec:reversibility` | Whether the action decided can be undone. For a decision covering several operations, the least reversible of them. |
| `dec:whyNow` | The reason the decision is put to the person at this time, in one or two sentences. |

## Values: Factual basis

| Term | Definition |
|---|---|
| `dec:SourcesCited` | The proposal names sources for its facts, and at least one was not read again for this decision. |
| `dec:SourcesRead` | Every fact the proposal relies on names a source, and each source was read for this decision. |
| `dec:Unsourced` | At least one fact the proposal relies on names no source. |

## Values: Nature of a decision

| Term | Definition |
|---|---|
| `dec:Alert` | A signal was put with no prepared proposal; the person decides whether anything is to be done. Criterion: no option was put. |
| `dec:Arbitration` | Two or more options were put; the person chooses. Criterion: at least two options were put. |
| `dec:Validation` | One prepared proposal was put; the person accepts it, changes it or refuses it. Criterion: exactly one option was put. |

## Values: Outcome

| Term | Definition |
|---|---|
| `dec:Amended` | The person accepted an option after changing it, or after asking for it to be changed. |
| `dec:Approved` | The person accepted an option as it was put. |
| `dec:Deferred` | The person set the decision aside without accepting or refusing; it may be put again. |
| `dec:Refused` | The person decided that no option put is to be carried out. |

## Values: Required oversight

| Term | Definition |
|---|---|
| `dec:Confirmation` | An authenticated person confirms in an open session. What was confirmed is known from the system's own log. |
| `dec:NoApproval` | The policy lets the action proceed without a person: a read, an observation. |
| `dec:Signature` | A person signs the exact content approved, its bytes or a digest of them, so that the approval can be checked afterwards without the system that collected it. |

## Values: Reversibility

| Term | Definition |
|---|---|
| `dec:Compensable` | The action cannot be undone, but a declared second action offsets its effect: a refund after a payment, a correction after a publication. |
| `dec:Irreversible` | No declared operation restores the earlier state or offsets the effect: a message read by its recipient, a disclosure, a deletion without a copy. |
| `dec:Reversible` | A declared operation restores the state that existed before the action, and the decider's organisation can run it alone. |
