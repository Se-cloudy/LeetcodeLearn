# 20230917:15:42 打家劫舍2
# 加个判断试试 再改一下边界
# 15:49 测试用例报错。各种边界的问题。检测没写对。
# 16:00 去吃饭了。。晚上再来。
# 如何判断首尾是否同存 想不出来
# 看了眼评论 分类 原来如此。分成0:-2和1:-1算max就行。5min
# 继续处理边界 10min
# AC
from typing import List

nums = [0]


def func(nums: List[int]) -> int:
    res = [nums[0]]
    if len(nums) == 1:
        return nums[0]
    else:
        res.append(max(nums[0], nums[1]))
        for i in range(2, len(nums)):
            res.append(max(res[i - 1], res[i - 2] + nums[i]))
        return res[-1]


if len(nums) == 1:
    print(nums[0])
elif len(nums) < 4:
    print(max(nums))
else:
    print(max(func(nums[:-1]), func(nums[1:])))
