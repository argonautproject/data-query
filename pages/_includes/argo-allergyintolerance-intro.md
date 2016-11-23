#### U.S. Argonaut AllergyIntolerance Profile


##### Scope and Usage

This profile sets minimum expectations for the [AllergyIntolerance] resource to record, search and fetch allergies/adverse events associated with a patient.  It identifies the mandatory core elements, extensions, vocabularies and value sets which **SHALL** be present in the AllergyIntolerance resource when using this profile.

**Example Usage Scenarios:**

The following are example usage scenarios for the Argonaut AllergyIntolerance
profile:

-   Query for allergies belonging to a Patient
-   Query for all patients who have a specific allergy


##### Mandatory Data Elements and Terminology


The following data-elements are mandatory (i.e data MUST be present). These are presented below in a simple human-readable explanation.  Profile specific guidance and examples are provided as well.  The [**Formal Profile Definition**](#profile) below provides the  formal summary, definitions, and  terminology requirements.  

**Each AllergyIntolerance must have:**

1.  a status of the allergy
2.  a code which tells you what the patient is allergic to
3.  a patient

**Profile specific implementation guidance:**

* Representing No Known Allergies: No Known Allergies will be represented using the Argonaut AllergyIntolerance profile with appropriate negation code in AllergyIntolerence.code.


##### Examples

- [AllergyIntolerance-23](AllergyIntolerance-23.html)


[AllergyIntolerance]: http://hl7.org/fhir/allergyintolerance.html
