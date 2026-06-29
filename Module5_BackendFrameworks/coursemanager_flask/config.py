# 38. In config.py, define a Config class with SQLALCHEMY_DATABASE_URI, SECRET_KEY, and DEBUG settings.
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess-this-default-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///coursemanager.db'
    DEBUG = True

