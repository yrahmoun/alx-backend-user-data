#!/usr/bin/env python3
""" module for app.py """
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index() -> str:
    """ Base routei """
    msg = {"message": "Bienvenue"}
    return jsonify(msg)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
