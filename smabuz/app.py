from config import Config

from flask import Flask
from datetime import timedelta


#init app
app= Flask(__name__, template_folder='templates')
app.config.from_object(Config)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=60)
