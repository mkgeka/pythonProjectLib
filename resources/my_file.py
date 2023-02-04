#!/usr/bin/env python
def all(iterable):
    melement = 0
    for element in range(1,iterable):
        melement = melement + element
    return melement
output = all(10000000)
print(output)