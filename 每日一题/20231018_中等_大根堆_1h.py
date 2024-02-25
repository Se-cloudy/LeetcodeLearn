# 17.02
# 2530. 执行 K 次操作后的最大分数
import heapq
# 17.27 例程错误。。sorted一次之后取cel可能会改变有序性。。需要维护最值 最大堆。
# 19:30-19:50 学习了原地堆化的代码。大根堆。奇妙的封装函数。。不太理解。

import math
from typing import List


def func(nums: List[int], k: int) -> int:
    for i in range(len(nums)):
        nums[i] = - nums[i]
    heapq.heapify(nums)  # 默认是最小堆 所以取负值
    res = 0
    for j in range(k):
        res -= heapq.heapreplace(nums, nums[0]//3)
    return res


if __name__ == '__main__':
    num = [10, 4, 6, 8]
    kk = 3
    print(func(num, kk))
