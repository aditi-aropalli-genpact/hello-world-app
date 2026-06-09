# Hello World - Python Flask App
import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    debug = os.getenv('FLASK_DEBUG', 'false').lower() == 'true'
    host = os.getenv('FLASK_HOST', '127.0.0.1')
    app.run(debug=debug, host=host, port=5000)
