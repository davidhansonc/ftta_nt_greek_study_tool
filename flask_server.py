from flask import Flask, render_template, request, redirect
import smtplib
import csv
from email.message import EmailMessage
import db_interact


app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html", book="Matthew")

@app.route("/", methods=["GET"])
def dropdown():
    books = ["Matthew", "Mark", "Luke", "John"]
    return render_template("index.html", books=books)

# @app.route("/<string:page_name>")
# def show_page(page_name=None):
#     return render_template(page_name)


# @app.route('/', methods=['POST', 'GET'])
# def submit_form():
#     if request.method == 'POST':
#         try:
#             data = request.form.to_dict()
#             write_to_csv(data)
#             print('written to database')
#             send_email(data)
#             print('email sent')
#             return render_template('index.html')
#         except:
#             return 'something went wrong while processing.'
#     else:
#         return 'must have been a GET request'