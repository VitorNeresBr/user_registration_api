from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base, User
from auth import get_password_hash, verity_password
from pydantic import BaseModel
from typing import List
import uvicorn

Base.metadata.create_all(bind=engine)

app = FastAPI()

class UserCreate(BaseModel):
    name: str
    password: str
    cpf: str

