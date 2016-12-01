#### Complete Summary of the Mandatory Requirements

1.  One date in `MedicationOrder.dateWritten`
1.  One status in `MedicationOrder.status` which has an [required](http://hl7.org/fhir/terminologies.html#required) binding to:
-   [MedicationOrderStatus] value set
1.  One patient reference in `MedicationOrder.patient`
1.  One practitioner in `MedicationOrder.prescriber`
1.  One medication via `MedicationOrder.medicationCodeableConcept` or `MedicationOrder.medicationReference`   
     -  `MedicationOrder.medicationCodeableConcept` has an [extensible](http://hl7.org/fhir/terminologies.html#extensible) binding to [Medication Clinical Drug (RxNorm)]

  [Medication Clinical Drug (RxNorm)]: valueset-medication-codes.html
  [MedicationOrderStatus]: http://hl7.org/fhir/valueset-medication-order-status.html
[MedicationStatementStatus]: http://hl7.org/fhir/valueset-medication-statement-status.html
