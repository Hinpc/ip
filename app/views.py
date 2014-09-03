from flask import request, Response

from app import app

@app.route('/')
def index():
    resp = request.headers.environ['HTTP_X_REAL_IP'] + '\n'
    return Response(resp, mimetype='text/plain')
