#!/usr/bin/env python
def all(iterable):
    melement = 0
    for element in range(1,iterable):
        melement = melement + element
        print(melement)
    return melement
output = all(50)
print(output)