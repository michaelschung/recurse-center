from sqlalchemy import create_engine, text
from sqlalchemy.orm import DeclarativeBase
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from markupsafe import escape, Markup

# DB config
default = True
DIALECT = 'postgresql+psycopg2'
USERNAME = 'postgres' if default else 'michaelchung'
PASSWORD = 'password' if default else 'yay'
HOST = 'localhost'
PORT = 8000
DB_NAME = 'postgres'

# SQLAlchemy config
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

# Flask config
def create_app(name):
    app = Flask(name)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'{DIALECT}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'
    db.init_app(app)
    return app