#!/usr/bin/env python3


"""import modules"""
from flask import Flask, render_template, request
from flask_babel import Babel, _
from typing import Any


class Config:
    """Configuration class for app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False


babel = Babel(app)


@app.route('/')
def hmoe() -> Any:
    """diplay home page"""
    return render_template('1-index.html')


@babel.localeselector
def get_locale() -> str:
    """get locale language"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(debug=True)
