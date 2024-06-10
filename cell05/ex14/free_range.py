#!/usr/bin/env python3
import sys

if len(sys.argv) == 3:
    arr = []
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    for i in range(x, y + 1):
        arr.append(i)
    print(arr)
else:
    print("none")
