#!/usr/bin/env python3
"""Write a function called filter_datum that
returns the log message obfuscated"""
import logging
import re


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        """ Constructor method """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = list(fields)

    def format(self, record: logging.LogRecord) -> str:
        """filter values in incoming log records using filter_datum"""
        return filter_datum(
            self.fields,
            self.REDACTION,
            super().format(record),
            self.SEPARATOR)


def filter_datum(fields, redaction, message, separator):
    """returns the log message obfuscated"""
    return re.sub(f'({"|".join(fields)})=([^;{separator}]*)',
                  f'\\1={redaction}', message)
