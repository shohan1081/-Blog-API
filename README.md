# Blog-API
I built this project to strengthen my foundational knowledge of Django, PostgreSQL, Django Rest Framework (DRF), and JWT authentication. My goal was to carefully implement clean and well-structured code while covering all the core concepts of these technologies.

This is a simple Blog API where users can register, log in, and create, update, or delete their blog posts. I also added support for image uploads and pagination to give it a more real-world feel. To push myself a bit further, I went ahead and Dockerized the entire project to get some hands-on experience with production-ready setups.

I tried to keep things as close to a real-world application as possible and focused on clean code, good practices, and practical features.
-------------------------------------------------------------------------------------------------------------
How to Set Up and Run the Project:
Option 1: Run with Docker (Recommended)
Follow these steps to run the Blog API using Docker and Docker Compose. This is the easiest way to get everything running without installing dependencies manually.

Step 1: Clone the Repository
Open a terminal and run:
git clone https://github.com/shohan1081/-Blog-API.git
cd -Blog-API

tep 2: Build and Run the Containers
Make sure you have Docker and Docker Compose installed. Then run:
docker-compose up --build


This will:

Start a PostgreSQL database in a container

Build and run your Django API in another container

Expose the API at http://localhost:8000/

Step 3: Apply Migrations and Create Superuser (Optional)
Once the containers are running, in a new terminal, run:
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser


Environment Variables (used in Docker)
Docker will automatically use these from docker-compose.yml, but for reference:

DB_NAME=blog_api

DB_USER=postgres

DB_PASSWORD=postgres

DB_HOST=db

DB_PORT=5432

 That’s it! The API will be live at http://localhost:8000/ and ready to use.
-----------------------------------------------------------------------------------------
Manual Setup Instructions
Step 1: Clone the Repository
git clone https://github.com/shohan1081/-Blog-API.git
cd -Blog-API

Step 2: Create and Activate a Virtual Environment
For Windows:
python -m venv room1
room1\Scripts\activate
For macOS/Linux:
python3 -m venv room1
source room1/bin/activate

Step 3: Install Dependencies
pip install -r requirements.txt

Step 4: Set Up PostgreSQL
Make sure PostgreSQL is installed and running on your machine.
Then create a database and user that match the settings in your .env file.

Step 5: Configure Environment Variables
Create a .env file in the root directory with the following:
SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=blog_api
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432

Step 6: Run Migrations and Create Superuser
python manage.py migrate
python manage.py createsuperuser

Step 7: Start the Development Server
python manage.py runserver

Your API is now live at:http://127.0.0.1:8000/
------------------------------------------------------------------------------------------------------------
How to Use the API
Below is a list of all the available API endpoints with a short description of what each does. Authenticated routes require a valid JWT access token in the request headers.

🔐 Authentication
Method	Endpoint	Description
POST	/api/register/	Register a new user
POST	/api/token/	Obtain access and refresh tokens
POST	/api/token/refresh/	Refresh your access token

📝 Blog Post Operations
Method	Endpoint	Description
GET	/api/posts/	List all blog posts (paginated)
POST	/api/posts/	Create a new post (requires login)
GET	/api/posts/<id>/	Retrieve a specific post by ID
PUT	/api/posts/<id>/	Update a post (only by the post author)
DELETE	/api/posts/<id>/	Delete a post (only by the post author)

🖼️ Extra Features
🔒 JWT Authentication: Add your token to the header like this:

Authorization: Bearer <your-access-token>
🖼️ Image Uploads: Supported when creating or updating posts.

📄 Pagination: Automatically applied to the posts list view.
