#!/usr/bin/env python3
""" Auth module """
import bcrypt


def _hash_password(password: str) -> bytes:
    """ Method that takes in a password string arguments and returns bytes."""
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password with the salt
    return bcrypt.hashpw(password.encode('utf-8'), salt)
