#!/usr/bin/env python3
import sys
import re

if len(sys.argv) == 3 and re.findall(sys.argv[1], sys.argv[2]):
    str = re.findall(sys.argv[1], sys.argv[2])
    x = len(str)
    print(x)
else:
    print("none")
