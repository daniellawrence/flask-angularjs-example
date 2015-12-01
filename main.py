#!/usr/bin/env python
from flask import Flask, jsonify, send_from_directory
app = Flask(__name__)


@app.route('/api/v1/get_names')
def get_names():
    names = {'names':
             [
                 'fred',
                 'john',
                 'paul',
                 'greg'
             ]}
    return jsonify(names)

@app.route('/api/v1/get_people')
def get_people():
    people = {"people": [
        {'name': 'fred', 'age': 10},
        {'name': 'john', 'age': 20},
        {'name': 'paul', 'age': 30},
        {'name': 'greg', 'age': 40},
    ]}
    return jsonify(people)


@app.route('/api/v1/get_time')
def get_time():
    import time
    return jsonify({'time': time.time()})


@app.route('/')
def index():
    return send_from_directory("templates", "index.html")


if __name__ == '__main__':
    app.debug = True
    app.run(port=1234)
