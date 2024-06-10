#!/usr/bin/env python3

x = int(input("Enter a number less than 25:\n"))
if x < 26:
    while x < 26:
        print("Inside the loop, my variable is", x)
        x += 1
else:
    print("Error")