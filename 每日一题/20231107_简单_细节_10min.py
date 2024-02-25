#15.43
# 2586. 统计范围内的元音字符串数
# 怀疑要用前缀和求部分和。。先不管。好像不需要，只处理一次。
#15.51 例子报错 奇怪 哦 我傻了 用的是原来的序列进行遍历。。而且右边界是r+1
#15.55 AC

words = ["are","amy","u"]
left = 0
right = 2
# 输出：1

res = 0
ls = words[left:right+1]
for word in ls:
    if word[0] in {'a','e','i','o','u'} and word[-1] in {'a','e','i','o','u'}:
        print(word)
        res += 1
print(res)