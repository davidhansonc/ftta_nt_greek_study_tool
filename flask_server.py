from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models import db, NTVerses, BibleBooks
from pandas import read_csv
from create_verse_tables import assemble_df


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://gchapifzwomimb:5be1227606be09cdc5fc4cb50bcafff0d1d32ea8572c6a2a10912d5481f7e3c5@ec2-50-16-108-41.compute-1.amazonaws.com:5432/d923lfcqpkom3m"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://davidhansonc:@localhost:5432/na28_rcv"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


def insert_table_data():
    s = db.session()

    # Fill Bible book data if table is empty
    if len(s.query(BibleBooks).all()) == 0:
        print("No data in the table detected.")
        print("Initializing the table in database.")
        df = read_csv("./database_creation/verses/nt_book_data.csv", usecols=range(3), lineterminator="\n")
        df.to_sql(name="bible_books", con=db.engine, if_exists="append", index=False)

    # Input verses if table is empty
    if len(s.query(NTVerses).all()) == 0:
        print("No data in the table detected.")
        print("Initializing the table in database.")
        gk_df = read_csv("./database_creation/verses/nestle1904/nestle1904.csv", usecols=range(4), lineterminator="\n")
        rcv_df = read_csv("./database_creation/verses/recovery_version/rcv.csv", usecols=range(4), lineterminator="\n")
        total_df.to_sql(name="bible_books", con=db.engine, if_exists="append", index=False)


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
        # subject = "The Gospel of the Kingdom--Proving That Jesus Christ Is the King-Savior"
        text = None
        try:
            text = query_text(translation, book)
        except:
            text = "text not found"

        translations = ["Nestle 1904", "Recovery Version"]
        books = get_book_list()


        return render_template("text.html", selected_version=translation, selected_book=book, subject=subject, text=text, translations=translations)
    else:
        return home()


def get_book_list():
    book_list = BibleBooks.query.with_entities(BibleBooks.book).all()
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


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        insert_table_data()
    # app.run()
    app.run(debug=True)