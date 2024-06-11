#!/usr/bin/env python3

###### Here is the method ######
class hello :
    def upcase_it(self, str):
        return (str.upper())

meow = hello()
print(meow.upcase_it("hello"))

###### Here is the function ######
def upcase_it(str):
    return (str.upper())

print(upcase_it("hello"))
