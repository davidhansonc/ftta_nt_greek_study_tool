from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, NTVerses
from data import book_data


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://davidhansonc:@localhost:5432/na28_rcv"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def home():
    translations = ["Nestle 1904", "Recovery Version"]
    books = list(book_data.keys())

    return render_template("index.html", translations=translations, books=books)


@app.route("/", methods=["POST"])
def get_user_selection():
    try:
        if request.method == "POST":
            translation = request.form["translation"]
            book = request.form["books"]
            chapter = request.form["chapter"]
    except:
        return "something is wrong"


if __name__ == "__main__":
    app.run(debug=True)