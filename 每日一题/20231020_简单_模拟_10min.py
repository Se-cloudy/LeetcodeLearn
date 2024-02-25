# 16.42 热身。
# 2525.根据规则把箱子分类
# 16.55 封装 AC

def func(length: int, width: int, height: int, mass: int) -> str:
    volume = length * width * height
    res = 'Neither'

    if volume >= 1e9 or length >= 1e4 or width >= 1e4 or height >= 1e4:
        res = 'Bulky'
    if mass >= 100:
        if res == 'Bulky':
            res = 'Both'
        else:
            res = 'Heavy'
    return res


print(func(1000, 35, 700, 300))
