# coding=UTF-8
# 136. 只出现一次的数字
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        for i in range(1,len(nums)):
            result ^= nums[i]
        return result

a = Solution()
b = a.singleNumber([1,2,3,4,5,6,7,2,3,4,5,6,7,1,9])
print(b)

# 结果：９