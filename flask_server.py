from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, NTVerses, BibleBooks
from data import book_data
import create_verse_tables


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://davidhansonc:@localhost:5432/na28_rcv"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def home():
    translations = ["Nestle 1904", "Recovery Version"]
    books = list(book_data.keys())
    # chapters = list(range(1, book_data[to_display[1]] + 1))
    to_display=["Nestle 1904", "Matthew"]

    return render_template("index.html", to_display=to_display, \
        translations=translations, books=books)  # , chapters=chapters)


@app.route("/", methods=["POST", "GET"])
def display_text():
    if request.method == "POST":
        translation = request.form["translation"]
        book = request.form["books"]
        # chapter = request.form["chapter"]
        text = query_text(translation, book)

        to_display = [translation, book]
        translations = ["Nestle 1904", "Recovery Version"]
        books = list(book_data.keys())

        book_subject = "The Gospel of the Kingdom--Proving That Jesus Christ Is the King-Savior"

        return render_template("text.html", to_display=to_display, text=text, translations=translations, books=books, book_subject=book_subject)
    else:
        return home()


def query_text(query_version="Nestle 1904", query_book="Matthew", query_chapter="1"):
    if query_version == "Nestle 1904":
        verses = NTVerses.query.filter(NTVerses.book==query_book, NTVerses.chapter==query_chapter).with_entities(NTVerses.nestle1904).all()
    else:
        verses = NTVerses.query.filter(NTVerses.book==query_book, NTVerses.chapter==query_chapter).with_entities(NTVerses.recovery_version).all()
    verses = [verse[0] for verse in verses]

    verses_as_string = ''.join(verses)
    return verses_as_string


if __name__ == "__main__":
    # db.create_all()
    create_verse_tables.init_database()
    # app.run()
    app.run(debug=True)