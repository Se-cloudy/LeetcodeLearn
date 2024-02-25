"""
3. 无重复字符的最长子串 中等
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

zzl：以前做过的，十分钟写出来。上周余淮还和我一起做过。。
两分钟写完。。但是输出是4.。r-l不用加1了。
五分钟之内AC！和上次的写法不一样，抄下来
"""
import collections
from typing import List


def lengthOfLongestSubstring(self, s: str) -> int:
    # 用计数控制。略微优化时间。
    counts = {}
    l = 0
    r = 0
    res = 0
    for i in range(len(s)):
        while s[i] in counts:
            del counts[s[l]]
            l += 1
        counts[s[r]] = 1
        res = max(res, r - l + 1)
        r += 1
    return res

def func(s: str) -> int:
    res = 0
    left = right = 0
    for i, c in enumerate(s):
        while c in s[left:right]:
            left += 1
        right += 1
        res = max(res, right - left)  # r+1的顺序决定了这里不用再+1了
    return res


if __name__ == "__main__":
    x = "abcabcbb"
    y = 4
    prt = func(x)
    print(prt)
