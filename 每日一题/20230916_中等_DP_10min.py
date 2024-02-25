#20230917:15.21 昨天抄的 复习下
# 198 打家劫舍

#好耶 自己用正序DP写出来了 昨天抄的是后序DFS 高级 看不懂
#第一次提交报错哦 经典边界bug 长度为1要排除
#15:35 AC 还玩了一会手机

nums = [2,7,9,3,1]
#输出：4
res = []
res.append(nums[0])
if len(nums) == 1:
    print(nums[0])
else:
    res.append(max(nums[0],nums[1]))
    for i in range(2,len(nums)):
        res.append(max(res[i-1],res[i-2]+nums[i]))
    print(res[-1])