#!/usr/bin/python3
""" script that starts a Flask web application """

from flask import Flask, render_template

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
    return "C {new_string}"


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    new_string = text.replace("_", " ")
    return "Python " + new_string


@app.route('/number/<int:n>')
def number_text(n):
    """ display “n is a number” only if n is an integer """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def template_text(n):
    """ display a HTML page only if n is an integer """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
