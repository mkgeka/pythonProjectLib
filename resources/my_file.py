#!/usr/bin/env python
def all(iterable):
    element = 0
    for element in range(1,iterable):
        #print(element)
        element += 1
    return element
output = all(50)
print(output)