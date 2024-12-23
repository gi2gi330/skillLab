from flask import  render_template
from forms import Addbookform
from extensions import app
books = [{"name": "მათემატიკა 11", "img": "matematika11.jpg", "description": "", "id":0},
            {"name": "მათემატიკა 12", "img": "matematika12.jpg", "description": "", "id":1},
            {"name": "ფიზიკა 11", "img": "fizika11.jpg", "description": "", "id":2},
            {"name": "ფიზიკა 12", "img": "fizika12.jpg", "description": "", "id":3},
            {"name": "ფიზიკა 10", "img": "fizika10.jpg", "description": "", "id":4},
            {"name": "ფიზიკა 9", "img": "fizika9.jpg", "description": "", "id":5},
        {"name": "ფიზიკა 8", "img": "fizika8.jpg", "description": "", "id":6},
        {"name": "ფიზიკა 7", "img": "fizika7.jpg", "description": "", "id":7},]

@app.route('/')
def index():
    return render_template('index.html',)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/books')
def all_books():
    return render_template('books.html', books=books)

@app.route('/add_book')
def add_book():
    form = Addbookform()
    return render_template('add_book.html', form=form)