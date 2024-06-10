#!/usr/bin/env python3
import sys

if len(sys.argv) == 2:
    str = ""
    s = "z"
    for i in sys.argv[1]:
        if i == 'z':
            str += s
    if len(str) != 0:
        print(str)
    else:
        print("none")
else:
    print("none")
