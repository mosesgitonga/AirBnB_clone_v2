#!/usr/bin/python3
"""
flask basics routes
"""

from flask import Flask, render_template
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
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    """
    route with default value
    """
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """check if it is number
    """
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_page(n):
    """
    display page in template
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """if number in the url is even or odd
    """
    if n % 2 == 0:
        var = f'{n} is even'
    else:
        var = f'{n} is odd'
    return render_template('6-number_odd_or_even.html', n=n, var=var)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
