''DocumentReference Search Criteria''

Patient/[id]/$get-docrefs?start=[date]&end=[end]$type=[type]

operation-argonaut-patient-docref.xml

OperationDefinition/patient-docref

Document references may not exist but may needed be created "on-the-fly" in response to a DocumentQuery request.  In other words there MAY NOT be pre-existing indices or set of references to a patient's documents at the FHIR endpoint which would result in an empty bundle being returned when using a normal FHIR Query (`GET [base]/DocumentReference?patient=[id]`). For example, in some cases the documents themselves may not exist but can be generated when needed so a reference to them can be generated using this operation.

The 'autogen' operation takes the parameters:
- patient
- date or date range
- document type

and returns the DocumentReference(s) like a standard query using GET if the docuement references already exists.  if an existing non-indexed document exists or an "on-demand" document can be created based upon the input parameters, then new DocuementReference instance(s) will be created and returned in the search bundle. If no documents exist and an "on-demand" document cannot be created then the operation will return an empty search bundle.

,
		"OperationDefinition/patient-docref": {
			"base": "operation-patient-docref.html"
		}