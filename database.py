from sqlalchemy import Column, Integer, String, create_engine, false
from sqlalchemy.exc.declarative import declaratie_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'sqlite://./users.db'

engine = create_engine(DATABASE_URL, connect_args={'check_same_thread':False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declaratie_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    password = Column(String)
    cpf = Column(Integer, unique=True, index=True)

Base.metadata.create_all(bind=engine)
