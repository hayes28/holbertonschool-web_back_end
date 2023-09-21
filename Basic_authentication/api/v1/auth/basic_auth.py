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
