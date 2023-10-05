#!/usr/bin/env python3
""" 5. Mock logging in
"""

import contextlib
from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)

class Config:
    """ Babel configuration """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.before_request
def before_request():
    """ Before request
    """
    g.user = get_user()


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user():
    """ Returns a user dictionary or None if the ID cannot be found """
    try:
        return users.get(int(request.args.get('login_as')))
    except Exception:
        return None


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ GET /
    Return:
      - 1-index.html
    """
    return render_template('7-index.html')


@babel.localeselector
def get_locale():
    """ Determine best match for supported languages
    Return:
      - Best language
    """
    # Locale from URL parameters
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale

    # Locale from user settings
    usr = get_user()
    if usr and usr['locale'] in Config.LANGUAGES:
        return usr['locale']

    # Locale from request header
    return request.accept_languages.best_match(Config.LANGUAGES)


@babel.timezoneselector
def get_timezone():
    """ Determine time zone
    Return:
      - Timezone
    """
    timezone = request.args.get('timezone')
    if timezone and timezone in Config.LANGUAGES:
        with contextlib.suppress(Exception):
            return timezone
    # Timezone from user settings
    usr = get_user()
    if usr and usr['timezone']:
        with contextlib.suppress(Exception):
            return usr['timezone']
    # Timezone from request header
    with contextlib.suppress(Exception):
        return request.headers.get('timezone')
    # Default timezone
    return 'UTC'


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, threaded=True, debug=True)
