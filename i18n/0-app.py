#!/usr/bin/env python3
""" 0. Basic Flask app """
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ GET /
    Return:
      - 0-index.html
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
