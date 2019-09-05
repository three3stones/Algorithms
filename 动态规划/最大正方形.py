# 最大正方形
# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
# 示例：
# 输入:
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# 输出: 4

"""
构造一个动态规划的列表dp，假定dp[i][j]为一个正方形的右下角，
那么判断dp[i][j]他的上边dp[i - 1][j], 左边dp[i][j - 1],左上边 dp[i - 1][j - 1]是否也是1来判断是否能组成一个正方形

如果dp[i][j] 对应的其他点每一个点都是2，表示这几个点本身也都对应着一个正方形，所以dp[i][j] 所对应的最大正方形的边长就应该是2+1=3
对于最大正方形的边长ans,每次在点dp[i][j] 对应最大边长的时候和ans进行比较，取最大值即可。
"""
class Solution:
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        m,n = len(matrix),len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        ans = 0         # 存储最大边长
        for i in range(m):
            for j in range(n):
                dp[i][j] = int(matrix[i][j])
                if i and j and dp[i][j]:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                ans = max(ans, dp[i][j])
        
        return ans * ans, dp

if __name__ == "__main__":
    case = [[1,0,1,0,0],
            [1,0,1,1,1],
            [1,1,1,1,1],
            [1,0,1,1,1]]
    a = Solution()
    b = a.maximalSquare(case)
    print(b)

#   结果：
#  (9, [[1, 0, 1, 0, 0], 
#       [1, 0, 1, 1, 1], 
#       [1, 1, 1, 2, 2], 
#       [1, 0, 1, 2, 3]])