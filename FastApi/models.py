from sqlalchemy import Column, Integer, String, UniqueConstraint
from db import Base


class BookOrm(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    author=Column(String(255), nullable=False, index=True)
    publication_year=Column(Integer,nullable=False)
    ISBN = Column(String(64), nullable=False, unique=True)

__table_args = (
    UniqueConstraint("title", "author","publication_year", name='uq_title_author_year')
)

