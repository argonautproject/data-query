
**`GET/CarePlan?patient=[id]&category=careteam&status=active`**

Example:

[GET https://fhir-open-api-dstu2.smarthealthit.org/CarePlan?patient=1137192&category=careteam](todo.html)

*Support:* Mandatory to support search by patient, category and status.

*Implementation Notes:* Search for all current care team members for a patient. Fetches a bundle of all current CarePlan resource(s) with a careteam category for the specified patient. [(how to search by reference)], [(how to search by token)].

*Response Class:*

-   (Status 200): successful operation
-   (Status 400): invalid parameter
-   (Status 401/4xx): unauthorized request
-   (Status 403): insufficient scope

  [(how to search by reference)]: http://hl7.org/fhir/DSTU2/search.html#reference
  [(how to search by token)]: http://hl7.org/fhir/DSTU2/search.html#token
  [Composite Search Parameters]: http://hl7.org/fhir/search.html#combining
  [(how to search by date)]: http://hl7.org/fhir/DSTU2/search.html#date
