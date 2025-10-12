from flask import Flask
from .config import Config
from .extensions import db

from products.views import product_bp

app = Flask(__name__)
app.config.from_object(Config())

app.register_blueprint(product_bp)

db.init_app(app)
with app.app_context():
    db.create_all()