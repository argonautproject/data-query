This profile sets minimum expectations for the [Observation] resource to record, search and fetch vital signs associated with a patient. It identifies which core elements, extensions, vocabularies and value sets **SHALL** be present in the resource when using this profile.

**Example Usage Scenarios:**

The following are example usage scenarios for the Argonaut VitalSigns
profile:

-   Query for vital signs of a particular patient
-   Query for patients with a particular type of vital sign measurement

##### Mandatory Data Elements and Terminology


The following data-elements are mandatory (i.e data MUST be present). These are presented below in a simple human-readable explanation.  Profile specific guidance and examples are provided as well.  The [**Formal Profile Definition**](#profile) below provides the  formal summary, definitions, and  terminology requirements.  

**Each Observation must have:**

1.  a status
1.  a category code of 'vital-signs'
1.  a LOINC code which tells you what is being measured and is taken from the “LOINC Code” column in the table below.
1.  a patient
1.  a time indicating when the measurement was taken
1.  a numeric result value and standard UCUM unit which is taken from the “LOINC Code” column in the table below.
    -   note: if there is no numeric result then you have to supply a reason

**Profile specific implementation guidance:**

* This table represents a minimum set of vital sign concepts, the required LOINC codes, and UCUM units of measure codes used for representing vitals signs observations. These are [extensible] bindings and require that when a system support of any of these vital signs concepts, they must represent them using these codes. In addition, if you have a blood pressure observation, you must have both a systolic and a diastolic component, though one or both may have dataAbsentReason instead of a value.

* Alternate codes may be provided in addition to the standard LOINC and UCUM codes defined here.  For exsample, if a more specific code is recorded (method specific LOINC Codes, SNOMED CT concepts, system specific codes), both code listed below and the more specific code must be sent.  The examples illustrate using other codes as translations.

* Other profiles may make rules about which vital sign must be present or must be present as part of a panel.

---

Vital Sign Name | LOINC&nbsp;Code | UCUM Unit Code  | Notes
--- | --- | --- | ---
Vital Signs Panel| 8716-3 | — | This is the top-level grouping structure for a set of vital signs.  It has no value in Observation.valueQuantity ; instead, it just includes related links (with type=has-member) to the Observations in this set (e.g. respiratory rate, heart rate, BP).  Note that querying for the panel may miss individual results that are not part of an actual panel.
Respiratory Rate | 9279-1 |/min |
Heart rate | 8867-4 | /min |
Oxygen saturation | 59408-5  | % | 59408-5 (Oxygen saturation in Arterial blood by Pulse oximetry) replaces the deprecated code 2710-2 which had been listed in C-CDA.  
Body temperature | 8310-5 | Cel, [degF] |
Body height | 8302-2 | cm, [in_i] |
Body length | 8306-3 | cm, [in_i] | Like height, but lying down, typically this is used for infants
Head circumference | 8287-5 | cm, [in_i]|
Body weight | 29463-7 | g, kg,[lb_av]|
Body mass index | 39156-5 | kg/m2 |
Blood pressure systolic and diastolic | 55284-4 | — | This is a grouping structure. It has no value in Observation.valueQuantity but contains at least one component (systolic and/or diastolic).
Systolic blood pressure |8480-6 | mm[Hg] | Observation.component code for a blood pressure Observation
Diastolic blood pressure | 8462-4 | mm[Hg] | Observation.component code for a blood pressure Observation

---

[Observation]: http://hl7.org/fhir/observation.html
[extensible]: http://hl7.org/fhir/terminologies.html#extensible


#### Examples

- [observation-blood-glucose](observation-blood-glucose.html)
- [observation-blood-pressure](observation-blood-pressure.html)
- [observation-bmi](observation-bmi.html)
- [observation-bp-data-absent](observation-bp-data-absent.html)
- [observation-head-circumference](observation-head-circumference.html)
- [observation-heart-rate](observation-heart-rate.html)
- [observation-height](observation-height.html)
- [observation-length](observation-length.html)
- [observation-oxygen-saturation](observation-oxygen-saturation.html)
- [observation-respiratory-rate](observation-respiratory-rate.html)
- [observation-temperature](observation-temperature.html)
- [observation-vitals-panel](observation-vitals-panel.html)
- [observation-weight](observation-weight.html)
