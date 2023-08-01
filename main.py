import sqlalchemy, psycopg2
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

from models import create_tables

DSN = "postgresql://postgres:12345678@localhost:5432/books"
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

session.close()