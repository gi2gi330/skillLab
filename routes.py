from flask import  render_template, request, redirect
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash
from forms import *
from config import app, db
import os
from models import Book, User



@app.route('/')
def index():
    return render_template('index.html',)



@app.route('/about')
def about():
    return render_template('about.html')





@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if request.method == "POST":
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect("/login")
    return render_template('register.html', form=form)



@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
        return redirect("/")
    return render_template('login.html', form=form)



@app.route('/books')
def all_books():
    books = Book.query.all()
    print(books)
    return render_template('books.html', books=books)



@app.route('/add_book', methods=["GET", "POST"])
def add_book():
    form = Addbookform()

    if request.method == "POST":
        file_img = request.files['img']
        file_img.save(os.path.join(app.config['UPLOAD_FOLDER'], file_img.filename))
        file_pdf = request.files['pdf']
        file_pdf.save(os.path.join(app.config['UPLOAD_FOLDER'], file_pdf.filename))

        book = Book(name=form.name.data, img=file_img.filename, pdf=file_pdf.filename)
        db.session.add(book)
        db.session.commit()

        return redirect("/")
    return render_template('add_book.html', form=form)



@app.route('/opened_book/<int:book_id>')
def opened_book(book_id):
    selected_book= Book.query.get_or_404(book_id)
    return render_template('opened_book.html', selected_book=selected_book)



@app.route('/delete/<int:id>', methods=["GET", "POST"])
def delete(id):
    selected_book = Book.query.get_or_404(id)
    db.session.delete(selected_book)
    db.session.commit()
    return redirect("/books")


@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")



@app.route('/tips')
def tips():
    return render_template('tips.html')