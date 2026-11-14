# Vocabulary: `https://w3id.org/decision#`

Prefix `dec:`. Version 0.2.0. This page is written from [vocab/decision.ttl](vocab/decision.ttl), which governs.

## Classes

| Term | Definition |
|---|---|
| `dec:Decision` | A choice put to one accountable person, or made by that person, about whether and how an action is taken. One Decision has at most one outcome. |
| `dec:Option` | A course of action put to the person in a Decision. |

## Properties

| Term | Definition |
|---|---|
| `dec:affectsThirdParty` | True when the action, once taken, reaches a person or an organisation outside the decider's own: a message sent to them, a payment, a publication, a change to their data or their contract. |
| `dec:assumption` | Something taken as true without a source when the decision was put, and said to be so. Criterion: stated as an assumption in what was put; a fact with a source is not an assumption. |
| `dec:chosenOption` | The option the person retained. Absent when the outcome is Refused, Deferred or Escalated. |
| `dec:classifiedBy` | Who or what applied the policy: a person, or a named system applying declared rules. |
| `dec:classifiedUnder` | The policy, with its version, under which nature, reversibility and required oversight were assigned: an IRI, or an identifier the organisation publishes. A classification with no policy named is an opinion. |
| `dec:contextVersion` | The version of the facts the proposal was built from: an identifier, or a digest of their bytes. It lets a reader tell a decision taken on facts that had changed since. |
| `dec:deadline` | The time after which the decision has no object, or after which a stated consequence follows. Absent when none was stated: absence is not 'no deadline'. |
| `dec:decidedAt` | When the person gave the outcome. Never earlier than putAt. |
| `dec:decider` | The one accountable person the decision is put to, or who makes it: an IRI or an identifier the organisation publishes. |
| `dec:dependsOn` | Another decision whose outcome must be known before this one can be carried out. |
| `dec:execution` | What became of the action decided. Meaningful only when the outcome is Approved or Amended. |
| `dec:factualBasis` | How the facts the proposal relies on were sourced when the decision was put. |
| `dec:legalEffect` | True when the action creates, changes or ends a right or an obligation of a person, or similarly significantly affects that person. |
| `dec:magnitude` | The size of what is decided, as a number and a unit stated in the proposal (an amount and a currency, a number of people, a number of files). Absent when the proposal states none: absence is not zero. |
| `dec:nature` | What kind of choice was put, by the number of options put: none (Alert), one (Validation), two or more (Arbitration). |
| `dec:objective` | What the decision is meant to achieve, as stated in what was put to the person. |
| `dec:option` | An option put to the person. Criterion: it was on the screen or in the document the person decided from. |
| `dec:outcome` | What the person decided. Absent while the decision is open. |
| `dec:preparedBy` | Who or what prepared what was put to the decider: a person, or a named system. Criterion: the author of the options and of the recommendation, not of the final choice. |
| `dec:putAt` | When the decision was put before the person: shown on a screen, or sent. When only the sending is known, it is the sending. |
| `dec:rankInSession` | One, plus the number of decisions requiring a Confirmation or a Signature that the same person had already decided in the same authenticated session. |
| `dec:recommendationShown` | Whether the person saw the preparer's recommendation before committing to a choice. |
| `dec:recommendedOption` | The option whoever prepared the decision recommended, when one was recommended. It is one of the options put. |
| `dec:recordedIn` | A document that records this decision, named by an IRI or by a digest of its bytes. This vocabulary does not say what the record must contain, nor how it is verified. |
| `dec:requiredOversight` | The least a person had to do, under the policy named by classifiedUnder, before the action could proceed. |
| `dec:reversibility` | Whether the action decided can be undone. For a decision covering several operations, the least reversible of them. |
| `dec:reviewTrigger` | The condition under which the decision is to be put again: a date, an event, a threshold. |
| `dec:shownContent` | What the person decided from, as rendered: an IRI, or a digest of the bytes of the view or the document. When the oversight is a Signature, the signature should cover it. |
| `dec:sourcesOpened` | How many of the sources named in what was put the person opened between putAt and decidedAt, as counted by the system. Absent when the system does not count. |
| `dec:statedRisk` | A risk named in what was put to the person. Criterion: it was on the screen or in the document the person decided from; a risk known to the preparer and not shown is not stated. |
| `dec:successCriterion` | How it will be judged that the action did what was intended, stated before the action is taken. |
| `dec:urgency` | When the policy asks for the decision, in three bands. |
| `dec:whyNow` | The reason the decision is put to the person at this time, in one or two sentences. |

## Values: Execution

| Term | Definition |
|---|---|
| `dec:CarriedOut` | The action decided was completed and its success criterion, when one was stated, was met. |
| `dec:Failed` | The action decided began and did not complete, or its success criterion was not met, and its effects remain. |
| `dec:NotStarted` | The action decided has not begun. |
| `dec:Undone` | The action decided began, and its effects were then removed or offset. |

## Values: Factual basis

| Term | Definition |
|---|---|
| `dec:SourcesCited` | The proposal names sources for its facts, and at least one was not read again for this decision. |
| `dec:SourcesRead` | Every fact the proposal relies on names a source, and each source was read for this decision. |
| `dec:SourcesUnavailable` | A source the proposal names could not be read when the decision was put: not synchronised, access withdrawn, or deleted. Added in 0.2.0. |
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
| `dec:Escalated` | The person passed the decision to someone with more authority, without deciding it. Added in 0.2.0. |
| `dec:Refused` | The person decided that no option put is to be carried out. |

## Values: Required oversight

| Term | Definition |
|---|---|
| `dec:Confirmation` | An authenticated person confirms in an open session. What was confirmed is known from the system's own log. |
| `dec:NoApproval` | The policy lets the action proceed without a person: a read, an observation. |
| `dec:Signature` | A person signs the exact content approved, its bytes or a digest of them, so that the approval can be checked afterwards without the system that collected it. |

## Values: Recommendation shown

| Term | Definition |
|---|---|
| `dec:AfterChoice` | The person first committed to a choice; the recommendation was shown afterwards, and the person could still change. |
| `dec:BeforeChoice` | The recommendation was visible when the person began to choose. |
| `dec:NotShown` | No recommendation was shown to the person. |

## Values: Reversibility

| Term | Definition |
|---|---|
| `dec:Compensable` | The action cannot be undone, but a declared second action offsets its effect: a refund after a payment, a correction after a publication. |
| `dec:Irreversible` | No declared operation restores the earlier state or offsets the effect: a message read by its recipient, a disclosure, a deletion without a copy. |
| `dec:Reversible` | A declared operation restores the state that existed before the action, and the decider's organisation can run it alone. |

## Values: Urgency

| Term | Definition |
|---|---|
| `dec:Immediate` | The policy asks for the decision before the person takes up anything else: a deadline already passed, a blocked delivery, a critical signal. |
| `dec:Planned` | The decision can wait for a time the person sets aside for it. |
| `dec:SameDay` | The policy asks for the decision within the working day. |
