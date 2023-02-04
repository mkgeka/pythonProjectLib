#!/usr/bin/env python
def all(iterable):
    element = 0
    for element in range(1,iterable):
        melement = element + element
        print(melement)
    return melement
output = all(50)
print(output)