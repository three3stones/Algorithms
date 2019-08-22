# coding=UTF-8
# 62. 不同路径
# 一个机器人位于一个 m x n 网格的左上角
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角, 问总共有多少条不同的路径？

# 输入: m = 3, n = 2
# 输出: 3
# 解释:
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向右 -> 向下
# 2. 向右 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向右

"""
我们令 dp[i][j] 是到达 i, j 最多路径
动态方程：dp[i][j] = dp[i-1][j] + dp[i][j-1]
注意，对于第一行 dp[0][j]，或者第一列 dp[i][0]，由于都是在边界，所以只能为 1
例如 m=3 , n=2
dp = [[1, 1, 1], 
      [1, 0, 0]]
"""
class Solution:
    def uniquePaths(self, m, n):
        dp = [[1]*n] + [[1]+[0] * (n-1) for _ in range(m-1)]
        # print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

a = Solution()
b = a.uniquePaths(7,3)
print(b)