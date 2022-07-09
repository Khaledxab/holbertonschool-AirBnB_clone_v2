#!/usr/bin/python3
"""flask wa start"""
from flask import Flask
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
def pyisfun(text="is cool"):
    """4 point python text"""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


if __name__ == "__main__":
    app.run()
