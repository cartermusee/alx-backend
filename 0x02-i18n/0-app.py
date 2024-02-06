#!/usr/bin/env python3
"""module for flask app"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    """rendering the templates"""
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)