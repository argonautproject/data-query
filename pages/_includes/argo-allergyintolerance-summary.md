#### Summary of the Mandatory Requirements

1.  One patient reference in `AllergyIntolerance.patient`
1.  One Identification of a substance, or a class of substances, that is considered to be responsible for the adverse reaction risk in `AllergyIntolerance.code` which has an [extensible](http://hl7.org/fhir/terminologies.html#extensible) binding to:
    -    [Argonaut Substance-Reactant for Intolerance and Negation Codes](valueset-substance.html) value set
1.  One status in `AllergyIntolerance.status` which has an [required](http://hl7.org/fhir/terminologies.html#required) binding to:
        -   [AllergyIntoleranceStatus](http://hl7.org/fhir/valueset-allergy-intolerance-status.html) value set  
