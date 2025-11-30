# Books API — Generic Views

## Endpoints

GET /api/books/  
- List all books  
- Permissions: Public  

GET /api/books/<id>/  
- Retrieve a specific book  
- Permissions: Public  

POST /api/books/create/  
- Create a new book  
- Permissions: Authenticated users  

PUT /api/books/<id>/update/  
- Update a book  
- Permissions: Authenticated users  

DELETE /api/books/<id>/delete/  
- Delete a book  
- Permissions: Authenticated users  

## View Types Used
- ListAPIView
- RetrieveAPIView
- CreateAPIView
- UpdateAPIView
- DestroyAPIView

## Customizations
- Validation for duplicate titles
- perform_create() & perform_update() hooks
- Permission classes to protect write operations
