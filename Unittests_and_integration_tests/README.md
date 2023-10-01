# Unittests and Integration Tests

## Table of Contents

1. [Introduction](#introduction)
2. [Resources](#resources)
3. [Setup](#setup)
4. [Requirements](#requirements)
5. [Learning Objectives](#learning-objectives)
6. [Tasks](#tasks)

## Introduction

This project focuses on writing unit tests and integration tests for various Python functions and classes. The tests are written using Python's unittest framework.

## Resources

- [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)
- [unittest.mock — mock object library](https://docs.python.org/3/library/unittest.mock.html)
- [How to mock a readonly property with mock?](https://stackoverflow.com/questions/11836436/how-to-mock-a-readonly-property-with-mock)
- [parameterized](https://pypi.org/project/parameterized/)
- [Memoization](https://en.wikipedia.org/wiki/Memoization)

## Setup

### Virtual Environment

It's recommended to use a virtual environment to manage dependencies. You can set it up using the following commands:

```bash
python3 -m venv myenv
source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`
```

## Requirements

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7
- All files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- Your code should use the pycodestyle style (version 2.5)
- All your files must be executable
- All your modules, classes, and functions must have documentation

## Learning Objectives

- Understand the difference between unit and integration tests
- Learn common testing patterns such as mocking, parameterizations, and fixtures

## Tasks

### 0. Parameterize a unit test

- Familiarize yourself with the `utils.access_nested_map` function and write unit tests for it.
- [Code Example](./test_utils.py)

### 1. Parameterize a unit test

- Implement `TestAccessNestedMap.test_access_nested_map_exception`.
- [Code Example](./test_utils.py)

### 2. Mock HTTP calls

- Familiarize yourself with the `utils.get_json` function and write unit tests for it.
- [Code Example](./test_utils.py)

### 3. Parameterize and patch

- Read about memoization and write tests for `utils.memoize`.
- [Code Example](./test_utils.py)

### 4. Parameterize and patch as decorators

- Familiarize yourself with the `client.GithubOrgClient` class and write unit tests for it.
- [Code Example](./test_client.py)

### 5. Mocking a property

- Write tests for `GithubOrgClient._public_repos_url`.
- [Code Example](./test_client.py)

### 6. More patching

- Write tests for `GithubOrgClient.public_repos`.
- [Code Example](./test_client.py)

### 7. Parameterize

- Write tests for `GithubOrgClient.has_license`.
- [Code Example](./test_client.py)

### 8. Integration test: fixtures

- Write integration tests for `GithubOrgClient.public_repos`.
- [Code Example](./test_client.py)
