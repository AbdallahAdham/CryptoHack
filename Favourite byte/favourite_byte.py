#!/usr/bin/env python3

from pwn import *

hex_string = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

bytes_string = bytearray.fromhex(hex_string)

flag = ""

for i in range(256):
        xored = [chr(j ^ i) for j in bytes_string]
        flag = "".join(xored)
        if flag.startswith("crypto"):
            print(flag)

