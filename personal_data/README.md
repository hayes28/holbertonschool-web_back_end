# Personal Data Project

## Resources

### Read or Watch:

- [What Is PII, non-PII, and Personal Data?](https://piwik.pro/blog/what-is-pii-personal-data/)
- [Logging Documentation](https://docs.python.org/3/library/logging.html)
- [bcrypt package](https://github.com/pyca/bcrypt/)
- [Logging to Files, Setting Levels, and Formatting](https://www.youtube.com/watch?v=-ARI4Cz-awo)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- Examples of Personally Identifiable Information (PII)
- How to implement a log filter that will obfuscate PII fields
- How to encrypt a password and check the validity of an input password
- How to authenticate to a database using environment variables

## Requirements

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.5)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules, classes, and functions must be documented

## Tasks

### 0. Regex-ing

Write a function called `filter_datum` that returns the log message obfuscated.

### 1. Log Formatter

Copy the following code into `filtered_logger.py`.

### 2. Create Logger

Use `user_data.csv` for this task.

### 3. Connect to Secure Database

Database credentials should NEVER be stored in code or checked into version control.

### 4. Read and Filter Data

Implement a `main` function that takes no arguments and returns nothing.

### 5. Encrypting Passwords

User passwords should NEVER be stored in plain text in a database.

### 6. Check Valid Password

Implement an `is_valid` function that expects 2 arguments and returns a boolean.

## Repo:

- GitHub repository: holbertonschool-web_back_end
- Directory: personal_data
