from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

SQLALCHEMY_HOST= os.getenv('SQLALCHEMY_HOST')
SQLALCHEMY_NAME=os.getenv('SQLALCHEMY_NAME')
SQLALCHEMY_USER=os.getenv('SQLALCHEMY_USER')

class Config():
    """Flask configuration vars from .env file."""

    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    DEBUG = os.getenv('DEBUG')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost/Smabuz'
    TESTING = os.getenv('TESTING')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}@{}/{}'.format(SQLALCHEMY_USER,SQLALCHEMY_HOST ,SQLALCHEMY_NAME )
