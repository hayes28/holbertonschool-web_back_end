#!/usr/bin/env python3
""" Module of Authentication """
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'], strict_slashes=False)
def welcome():
    """ GET /
    Return:
      - JSON payload
    """
    return jsonify({"message": "Bienvenue"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
