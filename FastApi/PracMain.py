from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy.orm import Session

from db import Base,engine,SessionLocal
from models import BookOrm

app = FastAPI()

Base.metadata.create_all(bind=engine)

class Book(BaseModel):
    id: int
    title: str
    author: str
    publication_year: int
    ISBN: str


class UpdateBook(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    publication_year: Optional[int] = None
    ISBN: Optional[str] = None


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/addbooks", response_model=Book, status_code=201)
async def createBook(book: Book, db: Session=Depends(get_db)):
    if db.get(BookOrm,book.id):
        raise HTTPException(status_code=409, detail="book id already exist")
    
    title_exist = db.query(BookOrm).filter(BookOrm.title.ilike(book.title)).first()
    if title_exist:
        raise HTTPException(status_code=409, detail="Book title already exist")
    
    isbn_exist = db.query(BookOrm).filter(BookOrm.ISBN == book.ISBN).first()
    if isbn_exist:
        raise HTTPException(status_code=409, detail="ISBN already exist")
    
    db_book = BookOrm(
        id=book.id,
        title=book.title,
        author=book.author,
        publication_year=book.publication_year,
        ISBN= book.ISBN,
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    
    return Book(** {
        "id":db_book.id,
        "title":db_book.title,
        "author":db_book.author,
        "publication_year":db_book.publication_year,
        "ISBN":db_book.ISBN
    })
    
    # if any(b.id == book.id for b in books):
    #     raise HTTPException(status_code=409, detail="book id already exists")
    # if any(b.title.lower() == book.title for b in books):
    #     raise HTTPException(status_code=409, detail="book title is already exists")
    # books.append(book)
    # return book


@app.get("/getallbooks", response_model=List[Book])
async def get_all_books():
    return books


@app.get("/getbookbyid/{bookid}", response_model=Book)
async def get_book_by_id(bookid: int):
    for b in books:
        if b.id == bookid:
            return b
        raise HTTPException(status_code=404, detail="Book not found")


# @app.put("/updatebook", response_model=Book)
# async def UpdateBook(book_id: Book):
#     for b in books:
#         if b.id == book_id:
            