# 📘 Matrix Sols – Developer Task

This is a Django REST Framework-based project implementing a secure Notes API with authentication, filtering, searching, and pagination features.

## 🔧 Setup Instructions

1. *Clone the repository*
   git clone https://github.com/REDDIRANI1/notes-api.git
   cd notes_api

2. Create and activate a virtual environment
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

4. Apply migrations
   python manage.py migrate

5. Run the development server
   python manage.py runserver

🔐 Test Credentials
You can use the following demo user credentials:
Username: reddirani
Password: rani@123

📚 API Summary
🔑 Authentication
POST /token/ – Obtain access and refresh tokens
POST /token/refresh/ – Refresh access token

📝 Notes Endpoints
GET /notes/ – List notes (requires JWT token)
POST /notes/ – Create a new note
GET /notes/{id}/ – Retrieve a note
PUT /notes/{id}/ – Update a note
PATCH /notes/{id}/ – Update a note
DELETE /notes/{id}/ – Delete a note

🔍 Filtering, Search & Pagination
Search:
Use the query param ?search=keyword on GET /notes/ to search by title or content.

Pagination:
Each notes list is paginated (10 notes per page by default). Use ?page=2, ?page=3, etc

🧪 API Documentation
Interactive Swagger UI:
Visit: http://localhost:8000/docs/

OpenAPI Schema:
http://localhost:8000/api/schema/
