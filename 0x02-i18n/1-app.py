#!/usr/bin/env python3


"""import modules"""
from flask import Flask, render_template
from flask_babel import Babel
from typing import Any


class Config:
    """Configuration class for app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
Babel = Babel(app)
app.config.from_object(Config)


@app.route('/')
def hmoe() -> Any:
    """diplay home page"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True)
