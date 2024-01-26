#!/usr/bin/python3
"""
<IP Address> - [<date>]
"GET /projects/260 HTTP/1.1" <status code>
"""


import signal
import sys
import re
import time

regex = '^([0-9]?[0-9]?[0-9]\.){3}[0-9]?[0-9]?[0-9] \
- \[\S* \S*] "\S* \S* \S*" [2-5]0[0,1,3,4,5] [0-9]+$'
ipregex = '^([0-9]?[0-9]?[0-9]\.){3}[0-9]?[0-9]?[0-9]'
filesizeregex = '[0-9]+$'
statuscoderegex = '" [2-5]0[0,1,3,4,5]'
valid_status_code = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
    }
filesize = 0
lineindex = 0


def show():
    """display status"""
    print("File size: {}".format(filesize))
    for code, num in valid_status_code.items():
        if num:
            print("{}: {}".format(code, num))

try:
    for line in sys.stdin:
        lineindex += 1
        if re.match(regex, line):
            statuscode = re.search(statuscoderegex, line).group(0)[2:]
            filesize += int(re.search(filesizeregex, line).group(0))
            if statuscode in valid_status_code:
                valid_status_code[statuscode] += 1
        if lineindex % 10 == 0:
            show()
except Exception:
    pass
finally:
    show()
