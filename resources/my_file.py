#!/usr/bin/env python
from typing import List

def check(row_start:int, row_end:int, column_start:int, column_end:int) -> List[List[int]]:
    M = [[*range(row_start, row_end+1, 1)], [*range(column_start, column_end+1, 1)]]
    list = []
    for i in M[0]:
        Result = [item * i for item in M[1]]
        list.append(Result)
    pass
    return list
output = check(2,4,3,7)
print(output)