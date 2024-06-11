#!/usr/bin/env python3
import sys
import re

if len(sys.argv) == 3 and re.findall(sys.argv[1], sys.argv[2]):
    s = re.findall(sys.argv[1], sys.argv[2])
    x = len(s)
    print(x)
else:
    print("none")
