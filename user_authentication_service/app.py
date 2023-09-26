#!/usr/bin/env python3
""" Module of Authentication """
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth

AUTH = Auth()

app = Flask(__name__)
app.debug = True


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome():
    """ GET /
    Return:
      - JSON payload
    """
    return jsonify({"message": "Bienvenue"}), 200


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """ POST /users
    JSON body:
      - email
      - password
    Return:
      - JSON payload
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """ POST /sessions
    JSON body:
      - email
      - password
    Return:
      - JSON payload
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if not AUTH.valid_login(email, password):
        abort(401)
    session_id = AUTH.create_session(email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie("session_id", session_id)
    # print(f"Session ID set in cookie: {session_id}")
    return response


@app.route("/sessions", methods=["DELETE"])
def logout():
    """ DELETE /sessions
      JSON body:
        - session_id
      Return:
        - JSON payload
      """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id=session_id)
    if user:
        AUTH.destroy_session(user.id)
        return redirect("/")
    else:
        abort(403)


@app.route("/profile", methods=["GET"])
def profile():
    """ GET /profile
      JSON body:
        - session_id
      Return:
        - JSON payload"""
    session_id = request.cookies.get("session_id")
    # print(f"Debug: Session ID from cookie: {session_id}")
    user = AUTH.get_user_from_session_id(session_id=session_id)
    # print(f"Debug: User object: {user}")

    if user:
        return jsonify({"email": user.email})
    else:
        abort(403)


@app.route("/reset_password", methods=["POST"])
def get_reset_password_token():
    """ POST /reset_password
      JSON body:
        - email
      Return:
        - JSON payload"""
    email = request.form.get("email")
    try:
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset_token})
    except ValueError:
        abort(403)

@app.route("/reset_password", methods=["PUT"])
def update_password():
    """ PUT /reset_password
      JSON body:
        - email
        - reset_token
        - new_password
      Return:
        - JSON payload"""
    email = request.form.get("email")
    reset_token = request.form.get("reset_token")
    new_password = request.form.get("new_password")
    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"})
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
