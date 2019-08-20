# 136. 只出现一次的数字
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
# 说明：你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
# 输入: [4,1,2,1,2]
# 输出: 4

"""
使用位运算
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t = 0
        for i in nums:
            t ^= i
        return t^0

a = Solution()
b = a.singleNumber([4,1,2,1,2])
print(b)