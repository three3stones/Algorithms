# coding=UTF-8
# 最长连续递增序列
# 输入: [1,3,5,4,7]
# 输出: 3
# 解释: 最长连续递增序列是 [1,3,5], 长度为3。
# 尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。 


"""
求什么什么的连续序列，用DP。
dp[i]表示以nums[i]结尾的递增序列的长度。
状态转移方程很简单，

dp[0] = 0，
if dp[i+1] > dp[i]， dp[i+1] = 1 + dp[i]。这代表可以在前一个递增序列的基础上再延长一个数。
"""
class Solution:
    def findLengthOfLCIS(self,nums):
        if nums==[]:
            return 0
        N = len(nums)
        Dp = [1]*N
        for i in range(N-1):
            if nums[i+1] > nums[i]:
                Dp[i+1] = Dp[i] + 1
        return max(Dp)


a = Solution()
b = a.findLengthOfLCIS([5,6,7,1,2,3,4,1])
print(b)