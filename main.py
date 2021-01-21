import os
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy


port = int(os.environ.get('PORT', 5000))

app= Flask(__name__, template_folder='templates')
app.secret_key = "inventory-qwertymodel"
#database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/Products'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db= SQLAlchemy(app)

#product table
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

#createAccount
#login
@app.route("/", methods=['GET', 'POST'])
def login():
    error= None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials.'
        else:
            return redirect(url_for('index'))
    return render_template("login.html", error=error)

#Homepage
@app.route("/index")
def index():
    return render_template("index.html")

#ProductsPage
@app.route("/tables")
def tables():
    data = Products.query.all()
    return render_template("tables.html", products = data)
#AddProducts
@app.route("/tables", methods=['POST'])
def insert():
    if request.method == 'POST':
        code = request.form['code']
        name= request.form['name']
        quantity= request.form['quantity']
        price = request.form['price']

        product_data = Products(code, name, quantity, price)
        db.session.add(product_data)
        db.session.commit()

        flash('Products Entry Updated Successfully')
        return redirect(url_for('tables'))
#EditProducts
@app.route('/update', methods = ['GET', 'POST'])
def update():
    if request.method == "POST":
        my_data = Products.query.get(request.form.get('id'))
        my_data.name = request.form['name']
        my_data.code = request.form['code']
        my_data.quantity = request.form['quantity']
        my_data.price = request.form['price']

        db.session.commit()
        flash("Products Info Updated Successfully")
        return redirect(url_for('tables'))
#Delete Products
@app.route('/delete/<id>/' , methods=['GET','POST'])
def delete(id):
    my_data = Products.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Products Entry Deleted Successfully")
    return redirect(url_for('tables'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
