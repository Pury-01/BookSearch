#!/usr/bin/env python3
from flask import Flask
"""
Flask application
"""

app = Flask(__name__)


@app.route('/')
def home():
    """default home route
    """
    return "Welcome to BookSearch"


if __name__ == "__main__":
    app.run(debug=True)
