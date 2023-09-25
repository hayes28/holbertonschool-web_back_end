#!/usr/bin/env python3
"""
Main file
"""
from auth import Auth

# Create an instance of the Auth class
auth_instance = Auth()

# Call the _hash_password method on the instance
print(auth_instance._hash_password("Hello Holberton"))

