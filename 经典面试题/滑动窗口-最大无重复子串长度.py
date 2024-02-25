# 3. 无重复字符的最长子串

s = "abcabcbb"
# 输出: 3
counts = {}  # dict
left = 0
right = 0
res = 0
for i in range(len(s)):
    while s[i] in counts:
        del counts[s[left]]  # 和增加左指针的顺序不能反
        left += 1
    counts[s[right]] = 1
    res = max(res, right - left + 1)
    right += 1  # 最后再加
print(res)