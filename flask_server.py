from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
from models import db, NTVerses, BibleBooks
import pandas as pd


app = Flask(__name__)

database_conn = os.environ['DATABASE_URL']
# database_conn = "postgresql://davidhansonc:@localhost:5432/na28_rcv" 

app.config["SQLALCHEMY_DATABASE_URI"] = database_conn
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route("/")
def home():
    translations = ["Nestle 1904", "Recovery Version"]
    books = get_book_list()

    return render_template("index.html", selected_version="Nestle 1904", selected_book="Matthew", translations=translations, books=books)


@app.route("/", methods=["POST", "GET"])
def display_text():
    if request.method == "POST":
        translation = request.form["translation"]
        book = request.form["books"]
        subject = get_book_subject(book)
        text = None
        try:
            text = query_text(translation, book)
        except:
            text = "text not found"

        translations = ["Nestle 1904", "Recovery Version"]
        books = get_book_list()

        return render_template("text.html", selected_version=translation, selected_book=book, text=text, translations=translations, books=books, book_subject=subject)
    else:
        return home()


def get_book_list():
    book_list = BibleBooks.query.with_entities(BibleBooks.book).all()
    book_list = [book[0] for book in book_list]
    return book_list


def get_book_subject(book_selection):
    subject = BibleBooks.query.filter(BibleBooks.book==book_selection).with_entities(BibleBooks.subject).first()[0]
    return subject


def query_text(query_version="Nestle 1904", query_book="Matthew", query_chapter="1"):
    if query_version == "Nestle 1904":
        verses = NTVerses.query.filter(NTVerses.book==query_book, NTVerses.chapter==query_chapter).with_entities(NTVerses.nestle1904).all()
    else:
        verses = NTVerses.query.filter(NTVerses.book==query_book, NTVerses.chapter==query_chapter).with_entities(NTVerses.recovery_version).all()
    verses = [verse[0] for verse in verses]

    verses_as_string = ''.join(verses)
    return verses_as_string


def insert_table_data():
    s = db.session()

    # Fill Bible book data if table is empty
    if len(s.query(BibleBooks).all()) == 0:
        print("No book data in the table detected.")
        print("Initializing BibleBooks table in database.")

        df = pd.read_csv("./database_creation/verses/nt_book_data.csv", usecols=range(3), lineterminator="\n")
        df.to_sql(name="bible_books", con=db.engine, if_exists="append", index=False)
        print("Book data initialized")

    # Input verses if table is empty
    if len(s.query(NTVerses).all()) == 0:
        print("No verse data in the table detected.")
        print("Initializing NTVerses table in database.")
        
        gk_cols = ["book", "chapter", "verse", "nestle1904"]
        gk_df = pd.read_csv("./database_creation/verses/nestle1904/nestle1904.csv", delimiter="|", names=gk_cols, header=None, usecols=range(4), lineterminator="\n")

        rcv_cols = ["book", "chapter", "verse", "recovery_version"]
        rcv_df = pd.read_csv("./database_creation/verses/recovery_version/rcv.csv", delimiter="|", names=rcv_cols, header=None, usecols=range(4), lineterminator="\n")

        total_df = pd.merge(rcv_df, gk_df, how="outer", on=["book", "chapter", "verse"])
        print(total_df.head(-5))
        total_df.to_sql(name="new_testament", con=db.engine, if_exists="append", index=False)
        print("Book data initialized")


if __name__ == "__main__":
    with app.app_context():
        # NTVerses.__table__.drop(db.engine)
        db.create_all()
        insert_table_data()
    app.run()
    # app.run(debug=True)
