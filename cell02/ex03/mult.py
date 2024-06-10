#!/usr/bin/env python3

x = int(input("Enter the first number:\n"))
y = int(input("Enter the second number:\n"))
res = x * y
print(x, "x", y, "=", res)
if res < 0:
    print("The result is negative.")
elif res > 0:
    print("The result is positive.")
else:
    print("The result is positive and negative.")