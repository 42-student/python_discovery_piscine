#!/usr/bin/env python3
import sys

###### Here is the method ######
class toDown :
    def downcase_it(self, str):
        return (str.lower())

x = len(sys.argv)
if x > 1:
    doDo = toDown()
    for i in range(x - 1):
        print(doDo.downcase_it(sys.argv[i + 1]))
else:
    print("none")

###### Here is the function ######
def downcase_it(str):
    return (str.lower())

x = len(sys.argv)
if x > 1:
    for i in range (x - 1):
        print(downcase_it(sys.argv[i + 1]))
else:
    print("none")
