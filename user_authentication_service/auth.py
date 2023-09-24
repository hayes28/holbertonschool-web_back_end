#!/usr/bin/env python3
""" Auth module """
import bcrypt
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
            hashed_password = self._hash_password(password)
            return self._db.add_user(email, hashed_password)

    def _hash_password(self, password: str) -> bytes:
        """ Method that takes in a password
        string arguments and returns bytes."""
        # Generate a salt
        salt = bcrypt.gensalt()
        # Hash the password with the salt
        return bcrypt.hashpw(password.encode('utf-8'), salt)
