from flask import Flask, render_template, request, redirect
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

app = Flask(__name__)

@app.route("/text")
@bolder
def bye():
    return "bye!"


@app.route("/", methods=["GET"])
def home():
    translations = ["Nestle 1904", "Recovery Version"]
    books = ["Matthew", "Mark", "Luke", "John", "Acts", "Romans"]
    return render_template("index.html", translations=translations, books=books)


if __name__ == '__main__':
    app.run(debug=True)