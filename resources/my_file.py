#!/usr/bin/env python
def all(iterable):
    melement = 0
    for element in range(1,iterable):
        print(element)
        melement = melement * element
    return melement
output = all(10)
print(output)