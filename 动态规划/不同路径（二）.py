# 不同路径 II

# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
# 网格中的障碍物和空位置分别用 1 和 0 来表示。

# 输入:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# 输出: 2
# 解释:
# 3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右

"""
dp[i][j] 是到达 i, j 最多路径
动态方程：dp[i][j] = dp[i-1][j] + dp[i][j-1]
"""
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        m, n = len(obstacleGrid[0]), len(obstacleGrid)
        dp = [[0 for _ in range(m)]for _ in range(n)]
        
        for i in range(m):              # 第一行取值为1
            if obstacleGrid[0][i] != 1:
                dp[0][i] = 1
            else:
                break
        for j in range(n):              # 第一列取值为1
            if obstacleGrid[j][0] != 1: 
                dp[j][0] = 1
            else:
                break
            
        for i in range(1, n):           # 直接从第二行、第二列开始
            for j in range(1, m):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


if __name__ == '__main__':
    test= [
            [0,0,0],
            [0,1,0],
            [0,0,0]
                    ]
    a = Solution()
    b = a.uniquePathsWithObstacles(test)
    print(b)     