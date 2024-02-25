# 15. 三数之和

'''
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请

你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。


示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
'''

nums = [-1, 0, 1, 2, -1, -4]
# 0\特例
if len(nums) < 3:
    print('ff')
# 初始化处理
nums.sort()
res = []
# 1\双指针固定后两个数，遍历第一个数
for i in range(len(nums)):
    if nums[i] > 0:
        print('ff')
        break
    if i > 0 and nums[i] == nums[i - 1]:  # 对i去除重复
        continue
    L = i + 1
    R = len(nums) - 1
    while L < R:
        cur = nums[L] + nums[R] + nums[i]
        if cur == 0:
            res.append([nums[L], nums[R], nums[i]])
            while L < R and nums[L] == nums[L + 1]:
                L += 1
            while L < R and nums[R] == nums[R - 1]:
                R -= 1
            L += 1
            R -= 1
        elif cur > 0:
            R -= 1
        else:
            L += 1
