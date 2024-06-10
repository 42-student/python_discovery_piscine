#!/usr/bin/env python3
import sys
import re

x = len(sys.argv)
if x > 1:
    pattern = r"ism"
    for i in range (1, x):
        if re.search(pattern, sys.argv[i]):
            continue
        else:
            str = sys.argv[i] + pattern
            print(str)
else:
    print("none")
