#!/usr/bin/env python3
""" Create a class BasicAuth that inherits from Auth.
For the moment this class will be empty."""

from api.v1.auth.auth import Auth
import re
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """ BasicAuth class. """

    def extract_base64_authorization_header(self,
                                            authorization_header:
                                                str) -> str:
        """
        Extracts the Base64 part of the Authorization header
        for Basic Authentication.
        """
        if authorization_header is None or \
                type(authorization_header) is not str:
            return None
        if authorization_header.startswith('Basic '):
            return authorization_header[6:]
        return None

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """
        Decodes the Base64 value of the Authorization header.
        """
        import base64
        if base64_authorization_header is None or \
                type(base64_authorization_header) is not str:
            return None
        try:
            return base64.b64decode(
                base64_authorization_header.encode('utf-8')).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> (str, str):
        """
        Extracts user email and password from the Base64 value of the
        Authorization header.
        """
        if decoded_base64_authorization_header is None \
                or type(decoded_base64_authorization_header) != str \
                or not re.search(':', decoded_base64_authorization_header):
            return None, None
        return tuple(re.split(':', decoded_base64_authorization_header))

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> User:
        """
        Returns the User instance based on email and password.
        """
        # Check for None or if not a string
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        if users := User.search({'email': user_email}):
            return next((user for user in users
                         if user.is_valid_password(user_pwd)), None)
        else:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Overloads Auth and retrieves the User instance for a request.
        """

        # Get the Authorization header from the request
        auth_header = self.authorization_header(request)
        # Get the Base64 part of the Authorization header
        auth_header = self.extract_base64_authorization_header(auth_header)
        # Decode the Base64 part of the Authorization header
        auth_header = self.decode_base64_authorization_header(auth_header)
        # Get the user credentials from the Base64 part of the
        # Authorization header
        user_credentials = self.extract_user_credentials(auth_header)
        # Return the User instance based on his email and password
        user_email, user_pwd = user_credentials
        return self.user_object_from_credentials(user_email, user_pwd)
