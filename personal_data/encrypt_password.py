#!/usr/bin/env python3
"""Encrypting passwords"""
import bcrypt


def hash_password(password: str) -> bytes:
    """returns a salted, hashed password, which is a byte string"""
    # generate a salt
    salt = bcrypt.gensalt()
    # hash the password with the salt
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """returns a boolean"""
    # check if the password is valid
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        return True
    else:
        return False
