#!/usr/bin/env python3
""" Create a class BasicAuth that inherits from Auth.
For the moment this class will be empty."""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ BasicAuth class. """

    def extract_base64_authorization_header(self,
                                            authorization_header:
                                                str) -> str:
        """ that returns the Base64 part of the Authorization header
        for a Basic Authentication: """
        if authorization_header is None or \
                type(authorization_header) is not str:
            return None
        if authorization_header.startswith('Basic '):
            return authorization_header[6:]
        return None

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """ that returns the decoded value of a Base64 string
        base64_authorization_header: Base64 string to decode
        Return: the decoded value or None if fails """
        import base64
        if base64_authorization_header is None or \
                type(base64_authorization_header) is not str:
            return None
        try:
            return base64.b64decode(
                base64_authorization_header.encode('utf-8')).decode('utf-8')
        except Exception:
            return None
