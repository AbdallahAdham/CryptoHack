#!/usr/bin/env python3

from egcd import egcd

gcd, u, v = egcd(26513, 32321)


flag = "crypto{{{}, {}}}".format(u, v)

print(flag)

