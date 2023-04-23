#!/usr/bin/python3
"""Create A web application using flask"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """create an  index page for my web application"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """ Create an additional route to my web application"""
    return "HBNB"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000))
