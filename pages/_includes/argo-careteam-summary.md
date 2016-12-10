#### Complete Summary of the Mandatory Requirements

1.  One reference to a patient in `CareTeam.subject`
1.  A fixed `CareTeam.status` = "active"
1.  One category in `Careplan.category` which must have:
-    a fixed `Careplan.category.coding.system` = "[http://argonaut.hl7.org/]"
-    a fixed `Careplan.category.coding.code` = "careteam"
1.  One participant role for each careteam member in
    `CareTeam.participant.role`
    -  CarePlan.participant.role is bound to the [CareTeam Provider Role
Value Set] value set.
1.  Careteam members in `CareTeam.participant.member`

 [CareTeam Provider Role Value Set]: ValueSet-provider-role.html
[http://argonaut.hl7.org/]: ValueSet-argo-codesystem.html
