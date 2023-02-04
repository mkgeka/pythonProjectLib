#!/usr/bin/env python
def all(iterable):
    melement = 1
    for element in range(1,iterable):
        print(melement)
        melement = melement * element
    return melement
output = all(10)
print(output)