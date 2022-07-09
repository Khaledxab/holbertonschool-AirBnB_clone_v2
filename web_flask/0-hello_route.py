#!/usr/bin/python3
"""flask wa start"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def HelloHbnb():
    """0 point"""
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run()
