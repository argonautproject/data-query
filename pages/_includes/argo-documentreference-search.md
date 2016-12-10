

Typically, DocumentReference resources are used with document indexing systems, such as [IHE XDS]. However, document references may also may be created "on-the-fly" in response to a Document Query request.  In other words there MAY NOT be pre-existing indes of references to a patient's documents at the FHIR endpoint. This results in an empty bundle being returned when searching using a normal FHIR Query.  Therefore, the [$docref operation] has been defined to both create and fetch patient DocumentReference Resources.


The following search criteria describe fetching pre-indexed documents and those created "on-the-fly".


**Searching pre-indexed documents:**

*Clients*

A client has connected to a server and fetched references to documents for a patient using `GET [base]/DocumentReference?patient=[id]`

A client **SHOULD** be capable of connecting to a server and fetching references to documents for a patient searched by type and/or date using:`GET [base]/DocumentReference?patient=[id]{&type=[type]}{&period=[date]}`


*Servers*


A server is capable of returning at references to documents for a patient using:`GET [base]/DocumentReference?patient=[id]`

 A server **SHOULD** be capable of connecting to a server and fetching references to documents for a patient searched by type and/or date using:`GET [base]/DocumentReference?patient=[id]{&type=[type]}{&period=[date]}`


- A server has ensured that every API request includes a valid Authorization token, supplied via:Authorization: Bearer {server-specific-token-here}
- A server has rejected any unauthorized requests by returning an HTTP 401 Unauthorized response code.

----

**`GET [base]/DocumentReference?patient=[id]`**

*Support:* Mandatory to support search by patient.

*Implementation Notes:* Search for all documents for a patient. Fetches a bundle of all DocumentReference resources for the specified patient [(how to search by reference)].

*Response Class:*

- (Status 200): successful operation
- (Status 400): invalid parameter
- (Status 401/4xx): unauthorized request
- (Status 403): insufficient scope

Example:

[GET https://fhir-open-api-dstu2.smarthealthit.org/DocumentReference?patient=2169591](https://fhir-open-api-dstu2.smarthealthit.org/DocumentReference?patient=2169591)

------

**`GET [base]/DocumentReference?patient=[id]&type=[type]&period=[date]`**

*Support:* Optional to support search by patient and type and date range.

*Implementation Notes:* Fetches a bundle of all DocumentReference resources for the specified patient for a given time period and document type.  [(how to search by reference)], [(how to search by token)], and [(how to search by date)].

*Response Class:*

 - (Status 200): successful operation
 - (Status 400): invalid parameter
 - (Status 401/4xx): unauthorized request
 - (Status 403): insufficient scope

Example:

[GET https://fhir-open-api-dstu2.smarthealthit.org/DocumentReference?patient=2169591&type=34133-9&period=ge2016-01-01](https://fhir-open-api-dstu2.smarthealthit.org/DocumentReference?patient=2169591&type=34133-9&period=ge2016-01-01)

-----

**Searching documents using the [$docref operation]:**

Functional behavior of Server when responding to the $docref operation:

1. SHALL return at least a reference to CCD document, if available, but MAY provide references to other document types as well.
2. If a context date range is supplied the server SHOULD provide references to any document that falls within the date range
3. If no date range is supplied, then the server SHALL provide references to last or current encounter


*Clients*

A client has connected to a server and fetches document references for a patient:
 - `GET [base]/DocumentReference/$docref?patient=[id]`

A client **SHOULD** be capable of connecting to a server and fetching references for a patient searched by type and/or date using:
 - `GET [base]/DocumentReference/$docref?patient=[id]{&type=[type]}{&period=[date]
 }`


*Servers*

 A server is capable of returning at at least the most recent CCD document references and **MAY** provide most recent references to other document for a patient using:`GET [base]/DocumentReference/$docref?patient=[id]`


 A server **SHOULD** be capable of returning references to CCD documents and **MAY** provide references to other document types for a patient searched by type and/or date using:`GET [base]/DocumentReference/$docref?patient=[id]{&type=[type]}{&period=[date]
  }`


- A server has ensured that every API request includes a valid Authorization token, supplied via:Authorization: Bearer {server-specific-token-here}
- A server has rejected any unauthorized requests by returning an HTTP 401 Unauthorized response code.

-----

**`GET [base]/DocumentReference/$docref?patient=[id]`**

*Support:* Mandatory to support search by patient.

*Implementation Notes:* Search for CCD documents from the last encounter and MAY search for other document types from the last encounter as well. Fetches a bundle of DocumentReference resources for the specified patient [(how to search by reference)].

*Response Class:*

- (Status 200): successful operation
- (Status 400): invalid parameter
- (Status 401/4xx): unauthorized request
- (Status 403): insufficient scope

Example:

[todo](#.html)

----

**`GET [base]/DocumentReference?patient=[id]&type=[type]&period=[date]`**

*Support:* Optional to support search by patient and type and date range.

*Implementation Notes:* Search for the specified document types from the context period for a patient. Server returns at least CCD document references and MAY search for other document types as well. Fetches a bundle of all DocumentReference resources for the specified patient for a given time period and document type.  [(how to search by reference)], [(how to search by token)], and [(how to search by date)].

*Response Class:*

 - (Status 200): successful operation
 - (Status 400): invalid parameter
 - (Status 401/4xx): unauthorized request
 - (Status 403): insufficient scope

Example:

[todo](#.html)


[(how to search by reference)]: http://hl7.org/fhir/DSTU2/search.html#reference
[(how to search by token)]: http://hl7.org/fhir/DSTU2/search.html#token
[(how to search by date)]: http://hl7.org/fhir/DSTU2/search.html#date
[IHE XDS]: http://wiki.ihe.net/index.php?title=Cross-Enterprise_Document_Sharing
[$docref operation]: OperationDefinition-get-docref.html
