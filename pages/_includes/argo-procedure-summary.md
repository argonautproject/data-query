#### Complete Summary of the Mandatory Requirements

1.  One patient reference in `Procedure.patient`
1.  A status code in Procedure.status which has a [required](http://hl7.org/fhir/terminologies.html#required) binding to:
-  [ProcedureStatus] value set.
1.  One Identification of the procedure in `Procedure.code` which has:
    - which has an [extensible + max valueset](definitions.html#extensible--max-valueset-binding-for-codeableconcept-datatype) binding to the [Argonaut Procdure Type] valueset (SNOMED CT or CPT-4/HCPC for procedures).
    - MAY have a translation to [ICD-10-PCS] or [Code on Dental Procedures and Nomenclature (CDT Codes)].
1.  A date or a time period in `Procedure.performedDateTime` or `Procedure.performedPeriod`


  [Argonaut Procdure Type]: ValueSet-procedure-type.html
  [ICD-10-PCS]: http://www.icd10data.com/icd10pcs
  [Code on Dental Procedures and Nomenclature (CDT Codes)]: http://www.ada.org/en/publications/cdt/
  [ProcedureStatus]: http://hl7.org/fhir/ValueSet-procedure-status.html
