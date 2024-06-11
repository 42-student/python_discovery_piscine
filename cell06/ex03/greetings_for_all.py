#!/usr/bin/env python3
import sys

def greetings(name=None):
    if name is None:
        print("Hello, noble stranger.")
    elif isinstance(name, (float, int, list, dict, tuple)):
        print("Error! It was not a name.")
    else:
        print(f"Hello, {name}.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
