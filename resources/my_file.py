#!/usr/bin/env python
def all(iterable):
    for element in range(1,iterable):
        print(element)
        element += 1
    return element
output = all(50)
print(output)