# coding=UTF-8
# 268. 缺失数字
# 给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。
# 输入: [9,6,4,2,3,5,7,0,1]
# 输出: 8
# 你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?

class Solution:
    def missingvalue(self, nums):
        res = len(nums)
        for i in range(len(nums)):
            res ^= (i ^ nums[i])
        return res

a = Solution()
b = a.missingvalue([0,1,7,2,3,4,6])
print(b)
