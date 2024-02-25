'''
官方库是heapq 原地堆化是heapify
基础排序算法之一。必须掌握默写与应用。
'''


# coding=utf-8
def heapify(ls, n, i):
    # 当前坐标i
    cur = i  # 最大值维护
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and ls[cur] < ls[left]:
        cur = left
    if right < n and ls[cur] < ls[right]:
        cur = right
    # 上浮
    if cur != i:
        ls[i], ls[cur] = ls[cur], ls[i]
        heapify(ls, n, cur)


def heap_sort(ls):  # 堆排序主函数
    n = len(ls)
    for i in range(n, -1, -1):
        heapify(ls, n, i)
    # 调整为有序数组
    k = 12  # 第k个最大值
    for i in range(n - 1, 0, -1):
        ls[i], ls[0] = ls[0], ls[i]  # 最大值赋到末尾
        if i == n - k:
            print(ls[i])
        heapify(ls, i, 0)
    if k == n:  # 最小值 上面取不到
        print(ls[0])


if __name__ == '__main__':
    array = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
    heap_sort(array)
    print(array)