Laboratory results are grouped and summarized using the [DiagnosticReport] resource which typically reference [Observation] resource(s).  When lab test or lab panel, such as CBC, is ordered, a DiagnosticReport represents the order fulfillment and references each of the resulting discrete Observations within that panel.  Each Observation resource represents an individual laboratory test and result value, a “nested” panel (such as a microbial susceptibility panel) which references other observations, or rarely a laboratory test with component result values.  They can also be presented in report form or as free text. This profile sets minimum expectations for the DiagnosticReport resource to record, search and fetch laboratory results associated with a patient. It identifies which core elements, extensions, vocabularies and value sets **SHALL** be present in the resource when using this profile.

**Example Usage Scenarios:**

The following are example usage scenarios for the Argonaut DiagnosticReport profile:

-   Query for lab reports belonging to a Patient
-   Record a lab report for a specific Patient

##### Mandatory Data Elements and Terminology


The following data-elements are mandatory (i.e data MUST be present). These are presented below in a simple human-readable explanation.  Profile specific guidance and examples are provided as well.  The [**Formal Profile Definition**](#profile) below provides the  formal summary, definitions, and  terminology requirements.  

**Each DiagnosticReport must have:**

1.   a status
1.   a category code of 'LAB'
1.   a code (preferably a LOINC code) which tells you what is being measured
1.   a patient
1.   a time indicating when the measurement was taken
1.   a time indicating when the measurement was reported
1.   who issues the report

Each DiagnosticReport *SHOULD* have:

1.   at least one result (discrete observation or image or text representation of the entire result)

**Profile specific implementation guidance:**

* Additional codes that translate or map to the DiagnosticReport codes or category codes are allowed.  For example:
   -  providing both a local system codes and a LOINC code that it map to
   -  providing a more specific category codes such as “CH” (chemistry) in addition to the "LAB"  category code.
* Results represented purely by free text or report form may be represented using the valueAttachment element in Observation or alternatively using the presentedForm element in DiagnosticReport.

#### Examples

   - [DiagnosticReport-urinalysis](DiagnosticReport-urinalysis.html)
   - [DiagnosticReport-metabolic-panel](DiagnosticReport-metabolic-panel.html)
   - [DiagnosticReport-cbc](DiagnosticReport-cbc.html)

[Observation]:  http://hl7.org/fhir/observation.html
[DiagnosticReport]:  http://hl7.org/fhir/diagnosticreport.html
