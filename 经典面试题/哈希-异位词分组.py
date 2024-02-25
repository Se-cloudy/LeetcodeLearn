"""
49. 字母异位词分组 中等

给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
字母异位词 是由重新排列源单词的所有字母得到的一个新单词。

示例 1:
输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
示例 2:
输入: strs = [""]
输出: [[""]]

zzl: 如何检查是为异位词.用26位存储字母出现的频率吗。分类是哈希。唔。
1 伟大的库函数 暴力哈希
2 计数 和我的想法相似。实现细节。就是用出现次数作为key，替代排序罢了。
复杂度都很高。下次优化。
"""
import collections
from typing import List


def func1(self, strs: List[str]) -> List[List[str]]:
    mp = collections.defaultdict(list)

    for st in strs:
        key = "".join(sorted(st))
        mp[key].append(st)

    return list(mp.values())


def func2(self, strs: List[str]) -> List[List[str]]:
    mp = collections.defaultdict(list)

    for st in strs:
        counts = [0] * 26
        for ch in st:
            counts[ord(ch) - ord("a")] += 1
        # 需要将 list 转换成 tuple 才能进行哈希
        mp[tuple(counts)].append(st)

    return list(mp.values())


def func(strs: List[str]) -> List[List[str]]:
    mp = collections.defaultdict(list)
    for s in strs:
        ls = [0] * 26
        for i in s:
            ls[ord(i)-ord('a')] += 1
        key = tuple(ls)  # 不然就是list 不能作为key
        mp[key].append(s)  # warning不影响。更应该化成str
    # print(mp.values())

    return list(mp.values())


if __name__ == "__main__":
    x = ["eat", "tea", "tan", "ate", "nat", "bat"]
    y = 4
    prt = func(x)
    print(prt)
