# coding=UTF-8
#  经典二分法（有序查找算法）
#  给定一个排好序（升序）的列表与待查找的关键字，成功则返回其索引，失败则返回-1。

"""
两个需要注意的地方：
    １．  while left <= right:
    ２．　right = mid - 1　　和　　left = mid + 1
"""

def BinarySearch(arr, key):
    left = 0
    right = len(arr) -1     #　要用到索引
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > key:
            right = mid - 1             # 记得要减一
        elif arr[mid] < key:
            left = mid + 1              # 记得要加一　　　否则会出现死循环
        else:
            return mid
    return -1

print(BinarySearch([1,2,3,4,5],key=0))