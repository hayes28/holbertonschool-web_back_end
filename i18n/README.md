# i18n - Internationalization with Flask

## Table of Contents

1. [Introduction](#introduction)
2. [Resources](#resources)
3. [Learning Objectives](#learning-objectives)
4. [Tasks](#tasks)

## Introduction

This project focuses on implementing internationalization (i18n) in a Flask application. It covers setting up Flask-Babel, localizing templates, and handling time zones.

## Resources

- [Flask-Babel](https://flask-babel.tutorialspoint.com/)
- [Flask i18n tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n)
- [pytz](https://pythonhosted.org/pytz/)

## Learning Objectives

- Learn how to parametrize Flask templates to display different languages
- Learn how to infer the correct locale based on URL parameters, user settings, or request headers
- Learn how to localize timestamps

## Tasks

### 0. Basic Flask app

- Setup a basic Flask app with a single `/` route.
- [Code Example](./0-app.py)

### 1. Basic Babel setup

- Install and configure Flask-Babel.
- [Code Example](./1-app.py)

### 2. Get locale from request

- Determine the best locale from the request headers.
- [Code Example](./2-app.py)

### 3. Parametrize templates

- Use Flask-Babel to localize templates.
- [Code Example](./3-app.py)

### 4. Force locale with URL parameter

- Implement locale selection via URL parameters.
- [Code Example](./4-app.py)

### 5. Mock logging in

- Mock a user login system to test locale and time zone settings.
- [Code Example](./5-app.py)

### 6. Use user locale

- Prioritize user settings for locale selection.
- [Code Example](./6-app.py)

### 7. Infer appropriate time zone

- Implement time zone selection logic.
- [Code Example](./7-app.py)

Author: Heather Hayes
