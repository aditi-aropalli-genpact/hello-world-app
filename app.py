# Hello World - Python Flask App
import os
import logging
from flask import Flask, render_template
from flask_talisman import Talisman

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s: %(message)s'
)

app = Flask(__name__)

# Security headers: CSP, X-Frame-Options, X-Content-Type-Options, HSTS, Referrer-Policy
Talisman(
    app,
    force_https=False,  # Set True behind HTTPS reverse proxy
    content_security_policy={
        'default-src': "'self'",
        'style-src': "'self' 'unsafe-inline'"
    }
)

@app.route('/')
def hello():
    app.logger.info('Hello World page accessed from %s', os.getenv('REMOTE_ADDR', 'unknown'))
    return render_template('index.html')

if __name__ == '__main__':
    debug = os.getenv('FLASK_DEBUG', 'false').lower() == 'true'
    host = os.getenv('FLASK_HOST', '127.0.0.1')
    port = int(os.getenv('FLASK_PORT', '5000'))
    app.run(debug=debug, host=host, port=port)
