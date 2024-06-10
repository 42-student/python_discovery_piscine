#!/usr/bin/env python3

x = int(input("Enter a number:\n"))
y = 0
while y < 10:
    res = x * y
    print(y, "x", x, "=", res)
    y += 1