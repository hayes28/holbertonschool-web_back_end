#!/usr/bin/env python3
"""Write a function called filter_datum that
returns the log message obfuscated"""
import re


def filter_datum(fields, redaction, message, separator):
    """returns the log message obfuscated"""
    return re.sub(f'({"|".join(fields)})=([^;{separator}]*)',
                  f'\\1={redaction}', message)
