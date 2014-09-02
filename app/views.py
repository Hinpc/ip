from flask import request

from app import app

@app.route('/')
def index():
    return request.headers.environ['HTTP_X_REAL_IP']
