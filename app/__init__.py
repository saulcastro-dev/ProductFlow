import os
from dotenv import load_dotenv
from flask import Flask
from .models import db

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///datasabe.db'
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', os.urandom(32))

db.init_app(app)
with app.app_context():
    db.create_all()

from app import views