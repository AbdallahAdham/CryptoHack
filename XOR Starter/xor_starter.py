#!/usr/bin/env python3

"""
HINTS:
- The Python pwntools library has a convenient xor() function that can XOR together data of different types and lengths.
- But first, you may want to implement your own function to solve this.
"""

from pwn import *

# ====================================== Manual approach ===============================================

msg = "label"
flag1 = ""

for i in range(len(msg)):
    xored = ord(msg[i]) ^ 13
    flag1 += chr(xored)

print("crypto{"+flag1+"}")

# ======================================= Built-In approach ===============================================

flag2 = xor(msg, 13).decode("utf-8")

print("crypto{"+flag2+"}")
