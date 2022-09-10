#!/usr/bin/python3
""" script that starts a Flask web application """

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hellohbnb_text():
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb_text():
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    new_string = text.replace("_", " ")
    return "C " + new_string


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    new_string = text.replace("_", " ")
    return "Python " + new_string


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
