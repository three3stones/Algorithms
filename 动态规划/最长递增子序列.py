# coding=UTF-8
# 最长递增子序列　（LIS问题）
# 给定一个未经排序的整数数组，找到最长且连续的的递增序列。
# 输入: [1,3,5,4,7]
# 输出: 4
# 解释: 最长递增子序列是 [1,3,5,7], 长度为4。

"""
使用动态规划，复杂度为O(n*n)    用Dp[i]来保存从0-i的数组的最长递增子序列的长度。
nums = [5,2,8,6,3,6,9,7]
Dp  =  [1,1,2,2,2,3,4,4]
计算Dp[i]的值要对Dp[i]之前数值进行遍历，如果nums[i]>nums[j],则Dp[i] = max(Dp[i],Dp[j]+1)。
"""

class Solution:
    def LIS(self,nums):
        if nums==[]:
            return 0
        N = len(nums)
        Dp = [1]*N
        for i in range(N-1):
            for j in range(0,i+1):      # 对Dp[i]之前数值进行遍历
                if nums[i+1]>nums[j]:
                    Dp[i+1] = max(Dp[i+1],Dp[j]+1)
        return max(Dp)

a = Solution()
b = a.LIS([5,2,8,6,3,6,9,7])
print(b)

