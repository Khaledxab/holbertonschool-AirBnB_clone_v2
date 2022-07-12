#!/usr/bin/python3
"""flask wa start"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def HelloHbnb():
    """0 point"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """1 point"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cISfun(text):
    """third point c text methode """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pyISfun(text="is cool"):
    """4 point python text"""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    if isinstance(n, int):
        return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numberTemplate(n):
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def oddeven(n):
    if isinstance(n, int):
        return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run()
