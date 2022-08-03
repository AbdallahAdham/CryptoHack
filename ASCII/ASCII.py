#!/usr/bin/env python3

"""
HINTS:
- In Python, the chr() function can be used to convert an ASCII ordinal number to a character.
- The ord() function does the opposite.
"""
ascii_arr = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

flag = ""

for i in range(len(ascii_arr)):
    flag += chr(ascii_arr[i])

print(flag)