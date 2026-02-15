from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Database_url = "mysql+pymysql://books_user:Pass123@localhost:3306/books_db"

engine = create_engine(Database_url, echo=False, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False)
Base = declarative_base()
