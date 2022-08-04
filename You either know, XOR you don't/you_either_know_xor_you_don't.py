#!/usr/bin/env python3

"""
HINTS:
- Remember the flag format and how it might help you in this challenge!
"""
from pwn import *

hex_string = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

bytes_string = bytes.fromhex(hex_string)


flag_format = 'crypto{'

key = ""
for i in range(len(flag_format)):
    key += ''.join(chr(bytes_string[i] ^ ord(flag_format[i])))

key = "myXORkey"

flag = xor(bytes_string, key.encode()).decode("utf-8")

print(flag)




