from flask import Flask,render_template,redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, db
from models import Products,Users
from flask_login import login_user

#WELCOME PAGE ROUTE
@app.route("/")
def base():
    return render_template("base.html")

#HOME ROUTE
@app.route("/index")
def index():
    return render_template("index.html")

#PROFILE ROUTE
@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/signup")
def adduser():
    return render_template("signup.html")

@app.route("/login")
def loginuser():
    return render_template("login.html")

#SIGNUP ROUTE
@app.route("/signup", methods=['POST'])
def signup():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')

    user = Users.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address alrserMixin,eady exists')
        return redirect(url_for('base'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = Users(username=username,email=email,password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('index'))

#LOGIN ROUTE
@app.route("/login", methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = Users.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('login')) # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('index'))

#PRODUCTS TABLE ROUTE
@app.route("/tables")
def tables():
    data = Products.query.all()
    return render_template("tables.html", products = data)

#ADD ENTRY ROUTE
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

#EDIT ENTRY ROUTE
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

#DELETE ENTRY ROUTE
@app.route('/delete/<id>/' , methods=['GET','POST'])
def delete(id):
    my_data = Products.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Products Entry Deleted Successfully")
    return redirect(url_for('tables'))
