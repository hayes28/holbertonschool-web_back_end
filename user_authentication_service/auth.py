#!/usr/bin/env python3
""" Auth module """
from bcrypt import hashpw, gensalt
from user import User
from sqlalchemy.orm.exc import NoResultFound
from db import DB


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
            return self._db.add_user(email, self._hash_password(password))

    def _hash_password(self, password: str) -> str:
        """ Method that takes in a password
        string arguments and returns bytes."""
        return hashpw(password.encode(), gensalt())
