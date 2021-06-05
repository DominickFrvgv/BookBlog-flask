from os import path

basedir = path.abspath(path.dirname(__file__))

class Config:
    SECRET_KEY = 'secret'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(basedir, 'dev_database.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
