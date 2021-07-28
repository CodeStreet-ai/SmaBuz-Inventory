from flask import render_template,redirect, url_for, request, flash, session, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from app import app
from models import *


global COOKIE_TIME_OUT
COOKIE_TIME_OUT = 1800 #30 minutes timeout


#WELCOME PAGE
@app.route("/")
def base():
    return render_template("base.html")

#SIGNUP PAGE
@app.route("/signup")
def adduser():
    return render_template("signup.html")

#LOGIN PAGE
@app.route("/login")
def login():
    return render_template("login.html")

#HOME
@app.route("/index")
def index():
    if 'email' in session:
        username_sess = session['email']

        user_r = Users.query.filter_by(email=username_sess).first()
        data = Products.query.filter_by(product_id=user_r.id)
        sum_p = sum([price.price for price in data])
        return render_template("index.html", products = data,user_r=user_r,sum_p=sum_p)
    else:
        return redirect('/login')
#PROFILE
@app.route("/profile")
def profile():
    if 'email' in session:
        username_sess = session['email']
        user_r = Users.query.filter_by(email=username_sess).first()
        return render_template("profile.html",user_r=user_r)
    else:
        return redirect('/login')


#SIGNUP
@app.route("/signup", methods=['POST'])
def signup():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')

    user = Users.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('base'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = Users(username=username,email=email,password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('index'))

#LOGIN
@app.route('/login' , methods = ['POST'])
def login_submit():
    email = request.form['email']
    password = request.form['password']
    remember = request.form.getlist('remember')

    if 'email' in request.cookies:
        username = request.cookies.get('email')
        password = request.cookies.get('password')
        row = Users.query.filter_by(email = username).first()
        if row and check_password_hash(row.password, password):
            session['email'] = row.email
            return redirect('/tables')
        else:
            return redirect('/login')
    elif email and password:
        #check if entry exists
        row = Users.query.filter_by(email = email).first()
        if row:
            if check_password_hash(row.password, password):
                session['email'] = row.email
                if remember:
                    response= make_response(redirect('/'))
                    response.set_cookie('email' , email, max_age=COOKIE_TIME_OUT)
                    response.set_cookie('password', password, max_age = COOKIE_TIME_OUT)
                    response.set_cookie('remember','checked', max_age= COOKIE_TIME_OUT)
                    return response
                return(redirect('/tables'))
            else:
                flash('Invalid Password')
                return redirect('/login')
        else:
            flash('Invalid Email or Password')
            return redirect('/login')
    else:
        flash('Invalid Email or Password')
        return redirect('/login')


#LOGOUT
@app.route('/logout')
def logout():
    if 'email' in session:
        session.pop('email', None)
    return redirect('/')

#PRODUCTS TABLE
@app.route("/tables", methods=['GET', 'POST'], defaults= {"page" : 1 })
@app.route('/tables/<int:page>', methods=['GET', 'POST'])
def tables(page):
    if 'email' in session:
        page = page
        pages = 7
        username_sess = session['email']
        user_r = Users.query.filter_by(email=username_sess).first()

        #filter product => product_id (one -many relationship with users)
        #data = Products.query.filter_by(product_id=user_r.id)
        #data = Products.query.paginate(page,pages,error_out=False)
        data = Products.query.filter_by(product_id=user_r.id).order_by(Products.id.asc()).paginate(page,pages,error_out=False)
        return render_template("tables.html", products = data,user_r=user_r)
    else:
        return redirect('/login')


#ADD ENTRY ROUTE
@app.route("/tables", methods=['POST'])
def insert():
    if request.method == 'POST' and 'email' in session :

        username_sess = session['email']
        user_r = Users.query.filter_by(email=username_sess).first()

        code = request.form['code']
        name= request.form['name']
        quantity= request.form['quantity']
        price = request.form['price']

        product_data = Products(code, name, quantity, price,product_id=user_r.id)
        db.session.add(product_data)
        db.session.commit()

        flash('Products Entry Updated Successfully')
        return redirect(url_for('tables'))
    else:
        return redirect('/login')

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
