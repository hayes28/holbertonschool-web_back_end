# User Authentication Service

## Resources

- [Flask Documentation](https://flask.palletsprojects.com/en/latest/)
- [Requests Module](https://docs.python-requests.org/en/latest/)
- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

## Learning Objectives

- How to declare API routes in a Flask app
- How to get and set cookies
- How to retrieve request form data
- How to return various HTTP status codes

## Setup

Install `bcrypt`:

    ```$pip3 install bcrypt```

## Table of Contents

0. [User Model](#user-model)
1. [Create User](#create-user)
2. [Find User](#find-user)
3. [Update User](#update-user)
4. [Hash Password](#hash-password)
5. [Register User](#register-user)
6. [Basic Flask App](#basic-flask-app)
7. [Register User End-Point](#register-user-end-point)
8. [Credentials Validation](#credentials-validation)
9. [Generate UUIDs](#generate-uuids)
10. [Get Session ID](#get-session-id)
11. [Log In](#log-in)
12. [Find User by Session ID](#find-user-by-session-id)
13. [Destroy Session](#destroy-session)
14. [Log Out](#log-out)
15. [User Profile](#user-profile)
16. [Generate Reset Password Token](#generate-reset-password-token)
17. [Get Reset Password Token](#get-reset-password-token)
18. [Update Password](#update-password)
19. [Update Password End-Point](#update-password-end-point)

## User Model

Create a SQLAlchemy model named `User`.

[Code Example](./user.py)

## Create User

Complete the `DB` class to implement the `add_user` method.

[Code Example](./db.py)

## Find User

Implement the `DB.find_user_by` method.

[Code Example](./db.py)

## Update User

Implement the `DB.update_user` method.

[Code Example](./db.py)

## Hash Password

Define a `_hash_password` method.

[Code Example](./auth.py)

## Register User

Implement the `Auth.register_user` method.

[Code Example](./auth.py)

## Basic Flask App

Set up a basic Flask app.

[Code Example](./app.py)

## Register User End-Point

Implement the end-point to register a user.

[Code Example](./app.py)

## Credentials Validation

Implement the `Auth.valid_login` method.

[Code Example](./auth.py)

## Generate UUIDs

Implement a `_generate_uuid` function.

[Code Example](./auth.py)

## Get Session ID

Implement the `Auth.create_session` method.

[Code Example](./auth.py)

## Log In

Implement a login function.

[Code Example](./app.py)

## Find User by Session ID

Implement the `Auth.get_user_from_session_id` method.

[Code Example](./auth.py)

## Destroy Session

Implement `Auth.destroy_session`.

[Code Example](./auth.py)

## Log Out

Implement a logout function.

[Code Example](./app.py)

## User Profile

Implement a profile function.

[Code Example](./app.py)

## Generate Reset Password Token

Implement the `Auth.get_reset_password_token` method.

[Code Example](./auth.py)

## Get Reset Password Token

Implement a `get_reset_password_token` function.

[Code Example](./app.py)

## Update Password

Implement the `Auth.update_password` method.

[Code Example](./auth.py)

## Update Password End-Point

Implement the `update_password` function.

[Code Example](./app.py)
