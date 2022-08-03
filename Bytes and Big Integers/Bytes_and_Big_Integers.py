#!/usr/bin/env python3

"""
HINTS:
- Python's PyCryptodome library implements this with the methods bytes_to_long() and long_to_bytes().
"""

from Crypto.Util.number import *

big_integer = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

bytes_string = long_to_bytes(big_integer)

flag = bytes_string.decode("utf-8")

print(flag)