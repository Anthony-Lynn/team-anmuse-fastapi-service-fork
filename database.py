import os

from typing import cast
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

load_dotenv()  # reads .env into environment variables

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(cast(str, DATABASE_URL))
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


class Base(DeclarativeBase):
    pass
