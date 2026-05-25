# Hello World - Python Flask App
import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    # Read debug mode from environment variable — never enable in production
    debug = os.getenv('FLASK_DEBUG', 'false').lower() == 'true'
    # Bind to localhost in dev; use a WSGI server (gunicorn) in production
    host = os.getenv('FLASK_HOST', '127.0.0.1')
    port = int(os.getenv('FLASK_PORT', '5000'))
    app.run(debug=debug, host=host, port=port)
