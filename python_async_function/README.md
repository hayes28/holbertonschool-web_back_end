# Python - Async Programming

## Resources

**Read or Watch:**

- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)
- [asyncio - Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
- [random.uniform](https://docs.python.org/3/library/random.html#random.uniform)

## Learning Objectives

### General

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- `async` and `await` syntax
- How to execute an async program with asyncio
- How to run concurrent coroutines
- How to create asyncio tasks
- How to use the random module

## Requirements

### General

- **README:** A README.md file, at the root of the folder of the project, is mandatory
- **Allowed editors:** vi, vim, emacs
- **Environment:** All files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- **New Line:** All your files should end with a new line
- **Executability:** All your files must be executable
- **File Length:** The length of your files will be tested using `wc`
- **Shebang:** The first line of all your files should be exactly `#!/usr/bin/env python3`
- **Code Style:** Your code should use the pycodestyle style (version 2.5.x)
- **Type Annotations:** All your functions and coroutines must be type-annotated.

### Documentation

- **Modules:** All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- **Functions:** All your functions should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- **Note:** A documentation is not a simple word; it’s a real sentence explaining the purpose of the module, class, or method (the length of it will be verified)

## Tasks

### 0. The basics of async

Write an asynchronous coroutine that takes in an integer argument (max_delay, with a default value of 10) named `wait_random` that waits for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it.

### 1. Let's execute multiple coroutines at the same time with async

Import `wait_random` from the previous python file and write an async routine called `wait_n` that takes in 2 int arguments: `n` and `max_delay`.

### 2. Measure the runtime

Create a `measure_time` function that measures the total execution time for `wait_n(n, max_delay)`, and returns `total_time / n`.

### 3. Tasks

Write a function called `task_wait_random` that takes an integer `max_delay` and returns a `asyncio.Task`.

### 4. Tasks

Alter the code from `wait_n` into a new function `task_wait_n`. The code is nearly identical to `wait_n` except `task_wait_random` is being called.
