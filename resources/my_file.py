#!/usr/bin/env python
def all(iterable):
    for element in range(1,iterable):
        melement = melement + element
        print(melement)
    return melement
output = all(50)
print(output)