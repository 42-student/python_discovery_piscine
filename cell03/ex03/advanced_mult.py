#!/usr/bin/env python3
import sys

miau = len(sys.argv)
if (miau == 1):
    x = 0
    while x < 11:
        y = 0
        print("Table de %d: " % (x), end="")
        while y < 11:
            print(x * y, end=" ")
            y += 1
        print()
        x += 1
else:
    print("none")
