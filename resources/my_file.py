#!/usr/bin/env python
def all(iterable):
    element = 0
    for element in range(1,iterable):
        element = element + element
        print(element)
    return element
output = all(50)
print(output)