#!/usr/bin/env python
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
all(1)