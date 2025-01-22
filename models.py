import sqlite3
from config import db, app
from flask_login import UserMixin, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash


books = [{"name": "მათემატიკა 11", "img": "matematika11.jpg", "description": "", "pdf": "", "id":0},
            {"name": "მათემატიკა 12", "img": "matematika12.jpg", "description": "","pdf": "", "id":1},
            {"name": "ფიზიკა 11", "img": "fizika11.jpg", "description": "","pdf": "", "id":2},
            {"name": "ფიზიკა 12", "img": "fizika12.jpg", "description": "","pdf": "", "id":3},
            {"name": "ფიზიკა 10", "img": "fizika10.jpg", "description": "","pdf": "", "id":4},
            {"name": "ფიზიკა 9", "img": "fizika9.jpg", "description": "","pdf": "", "id":5},
        {"name": "ფიზიკა 8", "img": "fizika8.jpg", "description": "","pdf": "", "id":6},
        {"name": "ფიზიკა 7", "img": "fizika7.jpg", "description": "","pdf": "", "id":7},]


from flask_sqlalchemy import SQLAlchemy

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, )
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=False)

    def __init__(self, username, password, role="guest"):
        self.username = username
        self.password = generate_password_hash(password)
        self.role = role

login_manager = LoginManager(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(80), unique= False, nullable= False)
    img = db.Column(db.String(80), unique= False, nullable= False)
    pdf = db.Column(db.String(80), unique= False, nullable= False)

    def __repr__(self):
        return f'{self.id}: {self.name}'

if __name__ == '__main__' :

    with app.app_context():
        db.create_all()
        admin = User(username='admin', password='admin123', role='admin')
        user = User(username='user', password='123')
        db.session.add(admin)
        db.session.add(user)
        db.session.commit()
        for book in books:
            new_book = Book(name= book['name'],img= book['img'], pdf=book['pdf'] )
            db.session.add(new_book)
            db.session.commit()
