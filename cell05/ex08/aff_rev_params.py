#!/usr/bin/env python3
import sys

x = len(sys.argv)
if x > 2:
    while x != 1:
        print(sys.argv[x - 1])
        x -= 1
else:
    print("none")

