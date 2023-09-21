#!/usr/bin/env python3
""" Now you will create a class to manage the API authentication. """
from typing import List, TypeVar
from flask import request

User = TypeVar('User')

class Auth:
    """ Auth class. """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Returns False - path and excluded_paths will not be used. """
        return False

    def authorization_header(self, request=None) -> str:
        """ Returns None - request will not be used. """
        return None

    def current_user(self, request=None) -> User:
        """ Returns None - request will not be used. """
        return None
