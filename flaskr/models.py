from datetime import datetime
from . import db
from . import login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin ,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(60), unique=True, index=True)
    password_hash = db.Column(db.String(200))
    about_me = db.Column(db.Text())
    
    books = db.relationship('Book', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('Passwrod cant be readible')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'{self.email}, {self.username}, '

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key =True)
    title = db.Column(db.String(60))
    author = db.Column(db.String(60))
    rating = db.Column(db.Float(), nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f"Books=({self.title}, {self.author}, {self.rating})"
