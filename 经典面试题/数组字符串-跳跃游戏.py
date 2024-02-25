'''
给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。

每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:

0 <= j <= nums[i]
i + j < n
返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。

'''

# 一定要注意边界，[0]必须能测试通过
# 缝缝补补半天 还是抄gpt的标答吧。。简短清晰得让人类汗颜。。

nums = [2,1]
# 先讨论极端情况 [] [0]
if len(nums) < 2:
    print(0)

max_reach = nums[0]  # 动态 当前最大值
steps = 1
boundary = nums[0]  # 静态 边界限制

for i in range(1, len(nums)):
    if i > boundary:
        steps += 1   # 一段的一次选择。。
        boundary = max_reach
    max_reach = max(max_reach, i + nums[i])

print(steps)
