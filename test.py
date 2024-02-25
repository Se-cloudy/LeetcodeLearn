"""

"""
import collections
from typing import List
import numpy as np


def func(s: str) -> int:
    mp = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    for i in range(len(s) - 1):
        if mp[s[i]] > mp[s[i + 1]]:
            res += mp[s[i]]
        else:
            res -= mp[s[i]]
    res += mp[s[-1]]
    return res


if __name__ == '__main__':
    array = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
    print(func("LVIII"))
