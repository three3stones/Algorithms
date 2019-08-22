# coding=UTF-8
# 34. 在排序数组中查找元素

# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
# 你的算法时间复杂度必须是 O(log n) 级别。
# 如果数组中不存在目标值，返回 [-1, -1]。

# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]

"""
一看到算法时间复杂度必须是 O(log n) 级别，肯定想到是二分法。
但这里二分法需要变换一下    1. 设置左右两个指针进行二分法，当通过二分法搜寻到目标值时，左右指针合一，
                        2. 然后在合一的位置上分别向左向右遍历寻找是否还有和目标值相等的数。
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1,-1]
        elif target < nums[0] or target > nums[-1]:
            return [-1,-1]
        else:
            left,right = 0,len(nums)-1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1         
                elif nums[mid] < target:
                    left = mid + 1
                # 当找到相等的值时，把左右指针合并并分别向左向右依次遍历找出上下限
                elif nums[mid] == target:
                    left = right = mid
                    while left-1>=0 and nums[left-1] == target:
                        left -= 1
                    while right+1<=len(nums)-1 and nums[right+1] == target:
                        right += 1
                    return [left, right]
        return [-1,-1]

a = Solution()
b = a.searchRange([5,7,7,8,8,8],8)
print(b)