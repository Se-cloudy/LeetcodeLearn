# 做过的 昨天也是。
# 15.45
# 122. 买卖股票的最佳时机 II
# 15.49 AC 但是比原答案复杂。。
prices = [7,1,5,3,6,4]
#输出：7
res = 0
cur = prices[0]
for i in range(1,len(prices)):
    cur = min(cur, prices[i])
    if prices[i] - cur > 0:
        res += prices[i] - cur
        cur = prices[i]
print(res)