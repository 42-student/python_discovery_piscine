#!/usr/bin/env python3

def is_int(nb):
    try:
        float_nb = float(nb)
        int_nb = int(float_nb)
    except ValueError:
        return (False)
    else:
        return (float_nb == int_nb)

def is_float(nb):
    try:
        float_nb = float(nb)
    except ValueError:
        return (False)
    else:
        return (True)

x = input("Give me a number: ")
if is_int(x):
    print("This number is an integer.")
elif is_float(x):
    print("This number is a decimal.")
else:
    print("Fuck off bby!")
