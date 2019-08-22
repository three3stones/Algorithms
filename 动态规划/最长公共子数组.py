# coding=UTF-8
# 718. 最长重复子数组
# 给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
"""
运用动态规划的思想
"""
class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        max_num = 0     # 存储子串的长度，并随时更新
        dp = [[0 for i in range(len(B)+1)] for j in range(len(A)+1)]
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                    max_num = max(dp[i+1][j+1], max_num)
        return max_num

a = Solution()
b = a.findLength([1,2,3,2,1,0],[3,2,1,0,4,7])
print(b)
