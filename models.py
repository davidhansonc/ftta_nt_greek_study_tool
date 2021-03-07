from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import PrimaryKeyConstraint

db = SQLAlchemy()

class NTVerses(db.Model):
    __tablename__ = "new_testament"

    book = db.Column(db.String(), nullable=False)
    chapter = db.Column(db.Integer(), nullable=False)
    verse = db.Column(db.Integer(), nullable=False)
    recovery_version = db.Column(db.String())
    nestle1904 = db.Column(db.String())
    __table_args__ = (
            db.PrimaryKeyConstraint(book, chapter, verse),
        )


    def __init__(self):
        self.book = book
        self.chapter = chapter
        self.verse = verse
        self.recovery_version = recovery_version
    

class BibleBooks(db.Model):
    __tablename__ = "bible_books"

    id = db.Column("book_id", db.Integer, primary_key=True)
    book = db.Column(db.String(), nullable=False)
    chapters = db.Column(db.Integer(), nullable=False)
    subject = db.Column(db.String())


    def __init__(self):
        self.book = book
        self.chapter = chapter
        self.subject = subject