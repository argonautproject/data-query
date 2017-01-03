#### Complete Summary of the Mandatory Requirements

1.  One status in `Immunization.status` which has an [required](http://hl7.org/fhir/terminologies.html#required) binding to:
-  [Immunization Status] value set.
1.  One dateTime in `Immunization.date`
1.  One vaccine code in `Immunization.vaccineCode` which:
 -  has an [extensible + max valueset](definitions.html#extensible--max-valueset-binding-for-codeableconcept-datatype) binding to the [CVX] value set
 -  SHOULD have a translation to the [NDC] value set
1.  One patient in `Immunization.patient`
1.  One boolean value in `Immunization.wasNotGiven`
1.  One boolean value in `Immunization.reported`

  [Immunization Status]: ValueSet-vacc-status.html
  [CVX]: http://hl7.org/fhir/DSTU2/daf/valueset-daf-cvx.html
  [NDC]: ValueSet-ndc-vaccine-codes.html
