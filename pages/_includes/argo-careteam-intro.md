This profile sets minimum expectations for the [CarePlan] resource for identifying the Care team members associated with a patient. It identifies which core elements, extensions, vocabularies and value sets **SHALL** be present in the resource when using this profile. **Note:** in FHIR STU3 the new [CareTeam] resource is recommended.

**Example Usage Scenarios:**

The following are example usage scenarios for the Argonaut CareTeam profile:

-   Query for a Patient's CareTeam
-   Record or update a Patient's CareTeam


##### Mandatory Data Elements and Terminology

Since we are using the CarePlan Resource for identifying the Care team members, constraints on that resource are defined for this purpose only. i.e. creating a CareTeam profile using CarePlan. The following data-elements are mandatory (i.e data MUST be present). These are presented below in a simple human-readable explanation.  Profile specific guidance and examples are provided as well.  The [**Formal Profile Definition**](#profile) below provides the  formal summary, definitions, and  terminology requirements.  

**Each CareTeam must have:**

1.  a patient
1.  a status code
1.  a category code of "careteam"
1.  a participant role for each careteam members
1.  names of careteam members which can be:
    -   a practitioner (doctor, nurse, therapist)
    -   the patient
    -   a relative or friend or guardian
    -   an organization

**Profile specific implementation guidance:**

* none

#### Examples

   - [CareTeam-1](CarePlan-careteam-1.html)

[CarePlan]:  http://hl7.org/fhir/careplan.html

[CareTeam]:  http://hl7.org/fhir/2017Jan/careteam.html
