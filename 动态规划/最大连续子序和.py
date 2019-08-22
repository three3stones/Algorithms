# coding=UTF-8
# 53. 最大子序和
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
"""
解题思路：
1. 如果当前和大于0，则加上下一个数（当前和是正的 对后面的求和“有益处”）
2. 如果当前和小于或等于0，则将下一个数赋给当前和
3. 最后比较当前和与存储最大值的变量 取最大值
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums = 0
        max_num = nums[0]
        for cur in nums:
            if sums >= 0:
                sums += cur
            else:
                sums = cur
            max_num = max(max_num, sums)
        return max_num

n = [-2,1,-3,4,-1,2,1,-5,4]
a = Solution()
b = a.maxSubArray(nums = n)
print(b)