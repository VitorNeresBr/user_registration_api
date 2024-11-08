from sqlalchemy import Column, Integer, String, create_engine, false
from sqlalchemy.exc.declarative import declaratie_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.testing import fails
from sqlalchemy.testing.plugin.plugin_base import engines

DATABASE_URL = 'sqlite://./users.db'

engine = create_engine(DATABASE_URL, connect_args={'check_same_thread':False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declaratie_base()

