#### Complete Summary of the Mandatory Requirements

1.  One status in `Observation.status`which has an [required](http://hl7.org/fhir/terminologies.html#required) binding to:
    -   [ObservationStatus] value set.
1.  One code in `Observation.code`
    -   a fixed `Observation.code.coding.system`= http://loinc.org
    -   a fixed `Observation.code.coding.code`=72166-2
1.  One reference to a Patient in `Observation.subject`
1.  One DateTime ([instant]) in `Observation.issued`
1.  One `Observation.valueCodeableConcept`which has an [extensible + max valueset](definitions.html#extensible--max-valueset-binding-for-codeableconcept-datatype) binding to the [Smoking Status] value set.


  [ObservationStatus]: http://hl7.org/fhir/ValueSet-observation-status.html
  [instant]: http://hl7.org/fhir/datatypes.html#instant
  [Smoking Status]: ValueSet-observation-ccdasmokingstatus.html
