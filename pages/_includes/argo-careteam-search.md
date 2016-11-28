

-------------------------

**Clients**

-  A client is able to connect to a server and fetch all current care team members for a patient using `GET[base]/CarePlan?patient=[id]&category=careteam&status=active`

**Servers**

-  A server is capable of returning a patient's current care team members using `GET[base]/CarePlan?patient=[id]&category=careteam&status=active`


- A server has ensured that every API request includes a valid Authorization token, supplied via:Authorization: Bearer {server-specific-token-here}
- A server has rejected any unauthorized requests by returning an HTTP 401 Unauthorized response code.

-----------

**`GET/CarePlan?patient=[id]&category=careteam&status=active`**

*Support:* Mandatory to support search by patient, category and status.

*Implementation Notes:* Search for all current care team members for a patient. Fetches a bundle of all current CarePlan resource(s) with a careteam category for the specified patient. [(how to search by reference)], [(how to search by token)].

*Response Class:*

-   (Status 200): successful operation
-   (Status 400): invalid parameter
-   (Status 401/4xx): unauthorized request
-   (Status 403): insufficient scope

Example:

[GET https://fhir-open-api-dstu2.smarthealthit.org/CarePlan?patient=1137192&category=careteam](#.html)

  [(how to search by reference)]: http://hl7.org/fhir/DSTU2/search.html#reference
  [(how to search by token)]: http://hl7.org/fhir/DSTU2/search.html#token
  [Composite Search Parameters]: http://hl7.org/fhir/search.html#combining
  [(how to search by date)]: http://hl7.org/fhir/DSTU2/search.html#date
