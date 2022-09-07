from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

SQLALCHEMY_HOST= os.getenv('SQLALCHEMY_HOST') #SERVER
SQLALCHEMY_DB=os.getenv('SQLALCHEMY_DB')  #DBNAME
SQLALCHEMY_USER=os.getenv('SQLALCHEMY_USER') #USERNAME
SQLALCHEMY_PASSWORD=os.getenv('SQLALCHEMY_PASSWORD') #PASSWORD

class Config():
    """Flask configuration vars from .env file."""

    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    DEBUG = os.getenv('DEBUG')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/{}'.format(SQLALCHEMY_USER, SQLALCHEMY_PASSWORD ,SQLALCHEMY_HOST ,SQLALCHEMY_DB)
    TESTING = os.getenv('TESTING')
