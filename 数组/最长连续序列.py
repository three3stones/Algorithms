# coding=UTF-8
# 128. 最长连续序列
# 给定一个未排序的整数数组，找出最长连续序列的长度。
# 要求算法的时间复杂度为 O(n)

# 输入: [100, 4, 200, 1, 3, 2]
# 输出: 4
# 解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

"""
遍历每个数，若是起点数那么就找他的下一个维护最大值
"""

class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        res = 0
        for i in nums:
            y = i +1
            while y in nums:
                y += 1
            res = max(res, y - i)
        return res

a = Solution()
b = a.longestConsecutive([99,98,101,100, 4, 200,102, 1, 3, 2])
print(b)