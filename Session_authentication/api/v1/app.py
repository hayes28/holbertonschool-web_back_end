#!/usr/bin/env python3
"""
Route module for the API
"""

from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
# Create instance of Auth if AUTH_TYPE is set to 'auth'
auth = None
auth_type = getenv("AUTH_TYPE", "basic")
if auth_type == "auth":
    from api.v1.auth.auth import Auth
    auth = Auth()

if auth_type == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()

if auth_type == "session_auth":
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()


@app.errorhandler(401)
def unauthorized(error) -> str:
    """Unauthorized handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """Forbidden handler
    """
    return jsonify({"error": "Forbidden"}), 403


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.before_request
def before_request_func() -> str:
    """ Before request handler
    """
    if auth is None:
        return
    excluded_paths = ['/api/v1/status/',
                      '/api/v1/unauthorized/',
                      '/api/v1/forbidden/',
                      '/api/v1/auth_session/login/']
    if not auth.require_auth(request.path, excluded_paths):
        return

    if auth and (
            not any(request.path.startswith(excluded)
                    for excluded in excluded_paths) and
            (auth.authorization_header(request)
             is None and auth.session_cookie(request) is None)
    ):
        abort(401)
    user = auth.current_user(request)
    if user is None:
        abort(403)
    request.current_user = auth.current_user(request)


if __name__ == "__main__":
    app.debug = True  # Enable debug mode
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
