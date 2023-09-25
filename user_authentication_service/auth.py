#!/usr/bin/env python3
""" Auth module """
import bcrypt
from user import User
from sqlalchemy.orm.exc import NoResultFound
from db import DB
from uuid import uuid4
from typing import Type


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Method that registers and returns
        a new user if email isn’t listed."""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        """ Method that checks if a user exists
        and validates password."""
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8'),
                                  user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """ Method that creates a session ID for a user."""
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> Type[User]:
        """ Method that returns a User
        corresponding to a session ID or None """
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user.email
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """ Method that updates the corresponding
        user’s session ID to None."""
        try:
            self._db.update_user(user_id, session_id=None)
        except NoResultFound:
            return None


def _hash_password(password: str) -> bytes:
    """ Method that takes in a password
    string arguments and returns bytes."""
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password with the salt
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def _generate_uuid() -> str:
    """ Method that returns a string representation
    of a new UUID."""
    return str(uuid4())
