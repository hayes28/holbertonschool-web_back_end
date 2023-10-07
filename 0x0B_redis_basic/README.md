# Redis Basic

## Table of Contents

1. [Introduction](#introduction)
2. [Resources](#resources)
3. [Learning Objectives](#learning-objectives)
4. [Requirements](#requirements)
5. [Installation](#installation)
6. [Tasks](#tasks)

## Introduction

This project focuses on the basic usage of Redis for data storage and caching.

## Resources

- [Redis commands](https://redis.io/commands)
- [Redis python client](https://pypi.org/project/redis/)
- [How to Use Redis With Python](https://realpython.com/python-redis/)
- [Redis Crash Course Tutorial](https://www.youtube.com/watch?v=Hbt56gFj998)

## Learning Objectives

- Learn how to use Redis for basic operations
- Learn how to use Redis as a simple cache

## Requirements

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- Your code should use the pycodestyle style (version 2.5)
- All your modules, classes, and functions must be documented
- All your functions and coroutines must be type-annotated

## Installation

To install Redis on Ubuntu 18.04:

bash
```$ sudo apt-get -y install redis-server```
```$ pip3 install redis```
```$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf```

## Use Redis in a container
Redis server is stopped by default - when you are starting a container, you should start it with: ```service redis-server start```

## Tasks

### 0. Writing strings to Redis
- **Objective**: Create a Cache class with methods for storing and retrieving data in Redis.
- **File**: `exercise.py`

### 1. Reading from Redis and recovering original type
- **Objective**: Implement methods for data retrieval and type conversion.
- **File**: `exercise.py`

### 2. Incrementing values
- **Objective**: Implement a decorator to count the number of times methods are called.
- **File**: `exercise.py`

### 3. Storing lists
- **Objective**: Implement a decorator to store the history of inputs and outputs for methods.
- **File**: `exercise.py`

4. Retrieving lists
- **Objective**: Implement a function to display the history of calls for a particular method.
- **File**: `exercise.py`