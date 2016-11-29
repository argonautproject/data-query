#### Summary of the Mandatory Requirements

1.  One identifier in `DocumentReference.masterIdentifier`
1.  One reference to a patient in `DocumentReference.subject`
1.  One document type code in `DocumentReference.type` which is bound to [Document Type Value Set]
1.  One dateTime value in `DocumentReference.indexed`
1.  One status in `DocumentReference.status`
    -   DocumentReference.status is bound to [DocumentReferenceStatus] Value set (Code set)
1.  One url of the document in `DocumentReference.content.attachment`
    -   a mime type in `DocumentReference.content.attachment.contentType` which is bound to [MimeType] value set (code set)
    -   a url of the document in `DocumentReference.content.attachment.url`
1.  One format code in `DocumentReference.content.format` with an [extensible] binding to `[DocumentReference Format Code Set]`

SHOULD have:

1.  One dateTime value in `DocumentReference.created`
1.  One time period value in `DocumentReference.context.period`

  [Document Type Value Set]: http://hl7.org/fhir/valueset-c80-doc-typecodes.html
  [DocumentReferenceStatus]: http://hl7.org/fhir/valueset-document-reference-status.html
  [MimeType]: http://www.rfc-editor.org/bcp/bcp13.txt#
  [extensible]: Implementation_Guide#Extensible_binding_for_CodeableConcept_Datatype "wikilink"
  [DocumentReference Format Code Set]: http://hl7.org/fhir/valueset-formatcodes.html
  [FHIR Binary Resource]: http://hl7.org/fhir/binary.html
