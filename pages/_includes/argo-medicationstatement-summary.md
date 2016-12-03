#### Complete Summary of the Mandatory Requirements


1.  One patient reference in `MedicationStatement.patient`
1.  One date `MedicationStatement.dateAsserted`
1.  One status in `MedicationStatement.status` which has an [required](http://hl7.org/fhir/terminologies.html#required) binding to:
-   [MedicationStatementStatus] value set.
1.  One medication via `MedicationStatement.medicationCodeableConcept` or `MedicationStatement.medicationReference`   
-  `MedicationStatement.medicationCodeableConcept` has an [extensible](http://hl7.org/fhir/terminologies.html#extensible) binding to [Medication Clinical Drug (RxNorm)] value set.

#### Summary of the Must Support Requirements

1.  One date or period in `MedicationStatement.effectiveDateTime` or `MedicationStatment.effectivePeriod`


  [Medication Clinical Drug (RxNorm)]: valueset-medication-codes.html
  [MedicationOrderStatus]: http://hl7.org/fhir/valueset-medication-order-status.html
[MedicationStatementStatus]: http://hl7.org/fhir/valueset-medication-statement-status.html
