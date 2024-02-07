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
        except UnicodeDecodeError:
            return False
    return True

# def validUTF8(data):
#     expected_continuations = 0
#     for byte in data:
#         if expected_continuations == 0:
#             if (byte >> 5) == 0b110:
#                 expected_continuations = 1
#             elif (byte >> 4) == 0b1110:
#                 expected_continuations = 2
#             elif (byte >> 3) == 0b11110:
#                 expected_continuations = 3
#             elif (byte >> 7):
#                 return False
#         else:
#             if (byte >> 6) != 0b10:
#                 return False
#             expected_continuations -= 1
#     return expected_continuations == 0
