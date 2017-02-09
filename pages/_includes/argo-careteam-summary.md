#### Complete Summary of the Mandatory Requirements

1.  One reference to a patient in `CareTeam.subject`
1.  A status code in `CareTeam.status` which has a [required](http://hl7.org/fhir/terminologies.html#required) binding to the
[CarePlanStatus] value set.
1.  A category in `Careplan.category` which must have:
-    a fixed `Careplan.category.coding.system` = "[http://argonaut.hl7.org/]"
-    a fixed `Careplan.category.coding.code` = "careteam"
1.  One participant role for each careteam member in
    `CareTeam.participant.role` which has an [extensible + max valueset](definitions.html#extensible--max-valueset-binding-for-codeableconcept-datatype) binding to the to the [CareTeam Provider Role
Value Set] value set.
1.  Careteam members in `CareTeam.participant.member`

 [CareTeam Provider Role Value Set]: ValueSet-provider-role.html
[http://argonaut.hl7.org/]: ValueSet-argo-codesystem.html
[CarePlanStatus]: http://hl7.org/fhir/ValueSet-care-plan-status.html
