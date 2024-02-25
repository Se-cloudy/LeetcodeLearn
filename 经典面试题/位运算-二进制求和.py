'''
67. 二进制求和 简单
给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。

示例 1：
输入:a = "11", b = "1"
输出："100"
'''

# 别人的 模拟二进制求和
def addBinary(self, a: str, b: str) -> str:
    n = max(len(a), len(b))
    a, b, c = a.zfill(n)[::-1], b.zfill(n)[::-1], ['0'] * (n + 1)
    for i in range(n):
        if (a[i], b[i]) == ('0', '0'): continue
        cnt = (a[i], b[i], c[i]).count('1')
        if cnt == 1:
            c[i] = '1'
        elif cnt == 2:
            c[i], c[i + 1] = '0', '1'
        else:
            c[i], c[i + 1] = '1', '1'
    return ''.join(c[::-1]).lstrip('0') if c.count('1') else "0"

# 套函数实现
a = '11'
b = '1'
a = int(a, 2)
b = int(b, 2)
res = bin(a + b)
print(res[2:])
