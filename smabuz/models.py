from app import app
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)

class Users(db.Model):

    ''' Users Table'''

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100),unique=True)
    password = db.Column(db.String(100))
    product= db.relationship('Products', backref='users', lazy=True)

    def __init__(self, username,email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return "<Users {}>".format(self.id)

class Products(db.Model):

    '''Products Table'''

    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    name = db.Column(db.String(50))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    product_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)

    def __init__(self, code,name,quantity,price,product_id ):
        self.code = code
        self.name = name
        self.quantity = quantity
        self.price = price
        self.product_id =product_id

    def __repr__(self):
        return "<Products {}>".format(self.id)
