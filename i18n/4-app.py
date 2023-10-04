#!/usr/bin/env python3
""" 2. Get locale from request
"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """ Babel configuration """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ GET /
    Return:
      - 1-index.html
    """
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    requested_locale = request.args.get('locale')
    if requested_locale in app.config['LANGUAGES']:
        return requested_locale
    """ Determine best match for supported languages
    Return:
      - Best language
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, threaded=True, debug=True)
