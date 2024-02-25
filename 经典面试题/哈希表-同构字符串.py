# 205. 同构字符串
# 判断两个字符串是否可以一一映射（密码表）

# 不妨假设一一映射 做完之后验证是否还原就行 需要双向验证
# 2023.10.30 AC 时空复杂度高

s = "abc"
t = "egg"

res = False
mp1 = {}  # dict
mp2 = {}
for i in range(len(s)):
    mp1[s[i]] = t[i]
    mp2[t[i]] = s[i]
temp = ''
semp = ''
for i in range(len(s)):
    temp += mp1[s[i]]
    semp += mp2[t[i]]
if temp == t and semp == s:
    res = True
print(res)