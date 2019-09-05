# TOP K 问题  ------  快速排序
"""
复杂度：O(N*logK)
思路：
1.  快速排序代码：每一轮快排都会使当前的元素N放置到最终的正确位置中，且左边的数字都大于等于X，右边的元素都小于X　（逆序排序）
2.  若X的下标（降序排序）等于K，则X左方加上X本身为整个数组最大的K个元素，满足问题需求，返回结果；
    若X的下标（降序排序）大于K，则针对下标范围为 [X.index+ 1 : end] 的子数组进行快速排序，直到满足要求1；
    若X的下标（降序排序）小于K，则针对下标范围为 [start : X.index] 的子数组进行快速排序，直到满足要求1；
"""

# 逆序排序的快排，最后返回哨兵的索引位置
def quick_index(array, start, end):
    left, right = start, end
    key = array[left]
    while left < right:
        while left < right and array[right] < key:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] >= key:
            left += 1
        array[right] = array[left]

    array[left] = key
    # print("遍历到的位置："+ str(left))
    return left

# 比较哨兵的索引位置和ｋ值大小
def max_num(array, k):
    start, end = 0, len(array) - 1
    index = quick_index(array, start, end)
    while index != k:
        if index < k:
            index = quick_index(array, index+1, end)
        else:
            index = quick_index(array, start, index)

    return array[:k]

if __name__ == '__main__':
    list2 = [4, 7, 0, 9, 1, 5, 8, 9]
    res = max_num(list2,4)
    print(res)  # [9, 9, 8, 7]

# 遍历到的位置：5
# 遍历到的位置：1
# 遍历到的位置：2
# 遍历到的位置：3
# 遍历到的位置：4
# [9, 9, 8, 7]