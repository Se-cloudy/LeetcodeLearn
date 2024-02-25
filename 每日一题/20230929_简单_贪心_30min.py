# 9.29 13.02
# 中秋。努力做题。
# 605. 种花问题
# 13.10 还是直接写不对。，模型有问题。我再想想。
# 经典看评论。。简单贪心，贪心我是真不会啊。细节也总是写错。还要考虑头尾。

flowerbed = [1,0,0,0,1]
n = 2
#输出：true

for i in range(len(flowerbed)):
    if flowerbed[i] == 0:
        if (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
            n -= 1
            flowerbed[i] = 1
if n > 0:
    return False
else:
    return True