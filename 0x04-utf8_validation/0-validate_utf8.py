#!/usr/bin/python3
"""
UTF-8 Validation
"""

def validUTF8(data):
    """
    UTF-8 Validation
    """
    for b in data:
        try:
            bytes([b]).decode('utf-8')
            return True
        except UnicodeDecodeError:
            return False
