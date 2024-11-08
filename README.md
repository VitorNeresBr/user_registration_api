# user_registration_api
 An API created using FastAPI for registration with basic user authentication. With endpoints for creating, reading, updating and deleting users. Extras: Integrated with an SQLite database to store data.

# First steps!
 First I created the project folder using the commands: 
mkdir fastapi_crud_auth
cd fastapi_crud_auth

 Then I created a virtual environment, this is optional but recommended, for this I used:
python -m venv venv

 And finally I installed the dependencies:
pip install fastapi uvicorn sqlalchemy passlib

# Second step: Creating the project structure!

 I created the following files in the .py template:
main.py # Main API file
database.py # Database configuration and user template
auth.py # Authentication functions

# Step 3: Setting up the Database with SQLAlchemy
 I used DATABASE_URL to define the location of the database which will be SQLite. Here, sqlite:///./users.db means that the database will be saved in a file called users.db in the current folder.
 
 I used connect_args={"check_same_thread": False} to disable SQLite's internal check that can cause errors if we try to access the database from different threads.

 I used autocommit=False so that changes are not automatically saved. They will only be confirmed (saved) when we call commit().
 
 autoflush=False prevents the session from automatically trying to save changes to the database while you are making changes.

 Base will be the base class used to create models. All models will inherit from it. 

 
