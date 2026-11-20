# Beside DecPROV 2.0: where each term would sit

A reading by the author of this vocabulary, made on 14 November 2026 from `decprov.ttl` version 2.0 (modified
2019-08-20, SHA-256 beginning `b98ac47960eb6d18`), read in full. It is not an alignment the author of DecPROV has
seen, and no `owl:equivalentClass` or `skos:exactMatch` is asserted anywhere in this repository.

DecPROV 2.0 has two properties (`hadAnswer`, `hadQuestion`), the classes `DecisionInputData` and
`DecisionLogicExpression`, the Decision Ontology's `Question`, `DecisionMaking`, `Answer` and `Requirement`, and the
role `DecisionMaker`. It records decisions already made, as PROV. Version 2.0 removed `OptionSelection`.

| Here | In DecPROV 2.0 | Remark |
|---|---|---|
| `dec:Decision` | no single class: a `do:Question`, the `do:DecisionMaking` activity and the `do:Answer` it generated | this vocabulary describes the three as one thing put to a person |
| `whyNow`, `label` | on the `do:Question` | |
| `decider` | a `prov:Agent` in the role `do:DecisionMaker` | |
| `preparedBy` | a `prov:Agent` associated with an earlier activity | DecPROV has no term for who prepared |
| `putAt`, `decidedAt` | start and end of the `do:DecisionMaking` activity | |
| `chosenOption`, `outcome` | the `do:Answer` | |
| `option`, `recommendedOption` | none since `OptionSelection` was removed | |
| `factualBasis`, `contextVersion`, `sourcesOpened` | `DecisionInputData` used by the activity | DecPROV says what was used, not whether it was read |
| `classifiedUnder` | a `DecisionLogicExpression` (a `prov:Plan`) | |
| `recordedIn` | any `prov:Entity`, by `prov:wasDerivedFrom` | |
| `reversibility`, `affectsThirdParty`, `legalEffect`, `magnitude`, `requiredOversight`, `urgency`, `rankInSession`, `recommendationShown`, `execution` | none found | what this vocabulary adds |
