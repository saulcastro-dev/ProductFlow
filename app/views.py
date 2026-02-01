from flask import Blueprint, render_template, url_for, redirect

app_bp = Blueprint('app', __name__)

@app_bp.route('/')
def index():
    return render_template('index.html')