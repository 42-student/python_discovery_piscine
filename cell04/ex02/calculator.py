#!/usr/bin/env python3

x = int(input("Give me the first number: "))
y = int(input("Give me the second number: "))
print("Thank you!")
print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
if y == 0:
    print("Error. Division by zero is not possible.")
else:
    print(f"{x} / {y} = {int(x / y)}")
print(f"{x} * {y} = {x * y}")
