#!/usr/bin/env python3
""" Session Authentication-Handles all routes for the Session Authentication """
from api.v1.views import app_views
from flask import jsonify, request, abort, make_response


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ POST /api/v1/auth_session/login
    Return: User object JSON represented"""
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400

    if not password:
        return jsonify({"error": "password missing"}), 400

    # Importing User from models.user, using search method
    from models.user import User
    try:
        users = User.search({'email': email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404

    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]

    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    # Creating a session ID with the user.id
    from api.v1.app import auth
    session_id = auth.create_session(user.id)

    # Getting the SESSION_NAME from env variables
    from os import getenv
    session_name = getenv('SESSION_NAME')

    # Making a response with the user.email and setting the session cookie
    response = make_response(user.to_json())
    response.set_cookie(session_name, session_id)

    return response
