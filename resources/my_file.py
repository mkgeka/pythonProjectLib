#!/usr/bin/env python
from typing import Any, Dict, List, Set

def check(lst: List[Dict[Any, Any]]) -> Set[Any]:
    my_list2 = []
    for x in lst:
        my_list = []
        for i in x.values():
            my_list.append(i)
        my_list2.append(my_list[0])
    set(my_list2)
    pass
    return set(my_list2)
output = check(2,4,3,7)
print(output)