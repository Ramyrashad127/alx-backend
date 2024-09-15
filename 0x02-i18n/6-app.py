#!/usr/bin/env python3


"""import modules"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Any
from typing import Dict, Union


class Config:
    """Configuration class for app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False


babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """Get user or return None"""
    login_id = request.args.get('login_as')
    if login_id:
        user = users.get(int(login_id))
    else:
        user = None
    return user


@app.before_request
def before_request() -> None:
    """Before request method to find user"""
    user = get_user()
    g.user = user


@app.route('/')
def hmoe() -> Any:
    """diplay home page"""
    return render_template('5-index.html')


@babel.localeselector
def get_locale() -> str:
    """get locale language"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user['locale'] in app.config["LANGUAGES"]:
        return g.user['locale']
    header_locale = request.headers.get('locale', '')
    if header_locale in app.config["LANGUAGES"]:
        return header_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(debug=True)
