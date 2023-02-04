#!/usr/bin/env python
from typing import Union, List

ListType = List[Union[int, str]]


def get_fizzbuzz_list(n: int) -> ListType:
    even_numbers = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            even_numbers.append("FizzBuzz")
        elif i % 3 == 0:
            even_numbers.append("Fizz")
        elif i % 5 == 0:
            even_numbers.append("Buzz")
        else:
            even_numbers.append(i)
    return even_numbers
output = get_fizzbuzz_list(5)
print(output)