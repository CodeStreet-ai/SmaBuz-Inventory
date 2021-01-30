from app import db
from flask_login import UserMixin

#Products Model
class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    name = db.Column(db.String(50))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)

    def __init__(self, code,name,quantity,price):
        self.code = code
        self.name = name
        self.quantity = quantity
        self.price = price

#Users Model
class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(100),unique=True)
    password = db.Column(db.String(100))

    def __init__(self, username,email, password):
        self.username = username
        self.email = email
        self.password = password
