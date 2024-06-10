#!/usr/bin/env python3

string = input()
newString = ""
for x in string:
    if x.isupper() == True:
        newString += x.lower()
    elif x.islower() == True:
        newString += x.upper()
    elif x.isspace() == True:
        newString += x
    elif x.isdigit() == True:
        newString += x
print(newString)
