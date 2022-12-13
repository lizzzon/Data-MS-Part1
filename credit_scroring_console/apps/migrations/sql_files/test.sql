SELECT documents.current_type, citizenships.citizenship_name, documents.documents_number,
documents.issue_date, documents.expiration_date
FROM documents
INNER JOIN citizenships ON documents.citizenship_id = citizenships.id
INNER JOIN clients ON documents.id = clients.document_id
WHERE clients.id = 1;