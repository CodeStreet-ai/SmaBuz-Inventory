from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from config import Config


#init app
app= Flask(__name__, template_folder='templates')
app.config.from_object(Config)
db = SQLAlchemy(app)
