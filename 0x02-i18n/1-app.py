#!/usr/bin/env python3

"""Module for a basic flask app."""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__,
        template_folder='./templates'
)
babel = Babel(app, locale_selector=get_locale)


class Config:
    """set Babel's languages."""
    LANGUAGES = ["en", "fr"]


@app.route('/')
def hello():
    """Simple route."""
    return render_template(
            '0-index.html',
            h1='Hello world',
            title='Welcome to Holberton',
    )


if __name__ == "__main__":
    app.run()
