"""
https://zhuanlan.zhihu.com/p/687384946
题目描述
众所周知，在一些消费支付的场合中，往往有“支付宝九五折”的优惠。这天小苯来到了超市购买物品，一共有
种物品，每种物品只能购买一个，但有的物品支持优惠活动，有的并不支持。恰好本超市的结账是有“支付宝九五折”优惠的，小苯的支付宝余额还剩
元，他想知道他仅使用支付宝进行支付的话最多能买几件物品?
"""
import sys
# n, k = map(int, input().split())
# ls = list(map(int, input().split()))
# val = input()
# print(ls,val)
n, k = 3, 370
ls = [100, 90, 80]
val = ['1','0','0']
for i in range(n):
    if val[i] == '1':
        ls[i] *= 0.95
print(ls)
ls.sort()
cnt = 0
for i in ls:
    k -= i
    cnt += 1
    if k <= 0:
        break
print(cnt)
