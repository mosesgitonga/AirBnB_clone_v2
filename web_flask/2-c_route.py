#!/usr/bin/python3
"""
flask basics routes
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
        return hello hbnb
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    return hbnb
    """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def is_fun(text):
    """
    start a flask web application
    """
    text = text.replace('_',' ')
    return f"C {text}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
