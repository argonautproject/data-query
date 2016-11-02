#### U.S. Data Access Framework (DAF) Core DocumentReference Profile


##### Scope and Usage

This profile sets minimum expectations  for searching and fetching patient documents using the [DocumentReference Resource]. It is loosely based on the use case ITI-68 in [IHE MHD] specification.  It identifies the mandatory core elements, extensions, vocabularies and value sets which **SHALL** be present in the DocumentReference resource when using this profile.

**Example Usage Scenarios:**

The following are example usage scenarios for the DAF-Core AllergyIntolerance
profile:

-   Query for all documents belonging to a Patient
-   Query for clinical summary information about patients (access a patient's Continuity of Care Document (CCD) 


##### Mandatory Data Elements and Terminology


The following data-elements are mandatory (i.e data MUST be present). These are presented below in a simple human-readable explanation.  Profile specific guidance and an [example](#example) are provided as well.  The [**Formal Profile Definition**](#summary) below provides the  formal summary, definitions, and  terminology requirements.  

**Each DocumentReference must have:**

1.  an identifier for the document
2.  a patient
3.  a code describing the type of document
4.  when the reference was created
5.  a status
6.  an https address where the document can be retrieved
7.  a code identifying the specific details about the format of the document — over and above the content's MIME type

In addition it should have ( if available) :

1.  a document creation date

**Profile specific implementation guidance:**

- The https address may refer to a FHIR Binary Resource (i.e. [base]/Binary/[id]) address on the server
- The https address may have a parameter that identifies the patient (e.g. GET [url]?patient=[id]). Argonaut servers SHOULD not require this parameter, but for IHE compatibility reasons SHALL allow it to be provided, and SHALL check that it is correct if it is provided.


[DocumentReference Resource]: http://hl7.org/fhir/documentreference.html
[IHE MHD]: http://ihe.net/uploadedFiles/Documents/ITI/IHE_ITI_Suppl_MHD.pdf
