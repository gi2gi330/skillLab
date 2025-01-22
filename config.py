from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)

UPLOAD_FOLDER = "static"
app.config["SECRET_KEY"]= "gn230f2hnd03idbd03i03"
app.config['UPLOAD_FOLDER']= UPLOAD_FOLDER
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"

db = SQLAlchemy(app)
