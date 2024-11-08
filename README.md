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

# Third step: Setting up the database with SQLAlchemy
 I used DATABASE_URL to define the location of the database which will be SQLite. Here, sqlite:///./users.db means that the database will be saved in a file called users.db in the current folder.
 
 I used connect_args={"check_same_thread": False} to disable SQLite's internal check that can cause errors if we try to access the database from different threads.

 I used autocommit=False so that changes are not automatically saved. They will only be confirmed (saved) when we call commit().
 
 autoflush=False prevents the session from automatically trying to save changes to the database while you are making changes.

 Base will be the base class used to create models. All models will inherit from it. 

 This part of the code defines the User model, which will represent the users table in the database. Each instance of User will be a row in the users table.

 __tablename__ = "users" will set the table name to users.

 id = Column(Integer, primary_key=True, index=True): Sets the id column as the primary key, a unique identifier for each record.

 name = Column(String, index=True): Sets the name column, which will be a string (text).

 password = Column(String): Sets the password column, which will also be a string. This column will store the encrypted password of the users.

 cpf = Column(String, unique=True, index=True): Sets the cpf column, which stores the user's CPF as a string. With unique=True, we are ensuring that each CPF will be unique in the table.

 And for safety, we use Base.metadata.create_all(bind=engine): to physically create the database and the users table with the columns defined in the users.db file if it does not already exist.
 
