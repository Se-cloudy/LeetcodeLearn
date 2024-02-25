'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
请注意 ，必须在不复制数组的情况下原地对数组进行操作。

nums = [0,1,0,3,12]
输出: [1,3,12,0,0]

zzl：就算我知道是双指针我也不会。。题解都是奥数天才吗。。要长脑子了。。
'''
from typing import List


def fun1(ls:List[int])->None:
    # 双指针遍历，利用记录指针留下不是0的数，然后在末尾补上0即可。
    pt = 0
    for i in range(1, len(ls)):
        if ls[i]:
            nums[pt] = ls[i]
            pt += 1
    for j in range(pt, len(ls)):
        nums[j] = 0


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    fun1(nums)
    print(nums)
