#!/usr/bin/env python3
import sys

def shrink(s):
    x = slice(8)
    print(s[x])

def enlarge(s):
    while len(s) < 8:
        s += 'Z'
    print(s)

x = len(sys.argv)
if x > 1:
    for i in range (x - 1):
        if len(sys.argv[i + 1]) < 8:
            enlarge(sys.argv[i + 1])
        elif len(sys.argv[i + 1]) > 8:
            shrink(sys.argv[i + 1])
        else:
            print(sys.argv[i + 1])
else:
    print("none")
