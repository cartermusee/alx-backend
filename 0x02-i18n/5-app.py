#!/usr/bin/env python3
"""module for flask app and initraing a babel"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """class for babels configs"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """get locale func to get the language"""
    lc = request.args.get('locale')
    if lc in app.config['LANGUAGES']:
        return lc
    return request.accept_languages.best_match(app.config['LANGUAGES'])


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    """get user by id"""
    return users.get(user_id)


@app.before_request
def before_request():
    user_id = request.args.get('login_as')
    g.user = get_user(int(user_id)) if user_id else None


@app.route("/")
def index() -> str:
    """rendering the templates"""

    return render_template("5-index.html")


if __name__ == '__main__':
    app.run(debug=True)
