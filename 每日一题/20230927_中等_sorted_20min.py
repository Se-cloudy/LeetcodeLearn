# 回来了 努力每天两题 一共1h
# 1333. 餐厅过滤器
# 16.00-16.10 感谢计算机二级 sorted 和列表推导式真好用
#为啥报错。。服了，没看清楚。sorted的key多个情况。。
# 16.18 AC; 时间复杂度高。

# restaurants[i] = [idi, ratingi, veganFriendlyi, pricei, distancei]
restaurants = [[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]]
veganFriendly = 0
maxPrice = 50
maxDistance = 10
# 输出：[3,1,5]
res = []
# select
for i in restaurants:
    if (veganFriendly and (i[2] != veganFriendly)) or (i[3] > maxPrice) or (i[4] > maxDistance):
        pass
    else:
        res.append(i)
# sort
sres = sorted(res, key=lambda x: (x[1],x[0]), reverse=True)
rr = [row[0] for row in sres]
print(rr)
