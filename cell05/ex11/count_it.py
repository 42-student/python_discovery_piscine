#!/usr/bin/env python3
import sys

x = len(sys.argv)
if x > 1:
    print("parameters:", x - 1)
    for i in range(1, x):
        print(sys.argv[i] + ":", len(sys.argv[i]))
else:
    print("none")
