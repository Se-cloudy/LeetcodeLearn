'''
202. 快乐数 简单

编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」 定义为：
对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果这个过程 结果为 1，那么这个数就是快乐数。
如果 n 是 快乐数 就返回 true ；不是，则返回 false 。

示例 1：
输入：n = 19
输出：true
解释：
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''

# tmd哪里简单了。题解一种是哈希表（数字最大映射的也不过三位数），一种是破除循环（万能快慢指针）。
def fSum(n: int) -> int:
    res = 0
    while n > 0:
        digit = n % 10
        res += digit * digit
        n //= 10
    return res


def isHappy1(n: int) -> bool:
    """
    累加num各个位的平方和；最大的数为2^31-1, 十位数，取平方和最大的可能值是1999999999，和为730.不高。
    """
    set_ = set()  # 记录循环过程中产生的数
    # 一旦新得到的数已经生成过，说明产生了循环，直接退出
    while n not in set_:
        if n == 1:
            return True  # 数字为1，返回true
        set_.add(n)  # 记录生成的数
        n = fSum(n)  # 生成新的数
    return False


def isHappy2(n:int):
    # 快慢指针，重合的时候说明出现循环，检测是否为1导致的循环，输出结果
    slow = n
    fast = fSum(n)
    while slow != fast:
        slow = fSum(slow)
        fast = fSum(fast)
        fast = fSum(fast)
    print(slow,fast)
    if slow == 1:
        return True
    else:
        return False


if __name__ == "__main__":
    x = 19
    print(isHappy2(x))
