# coding=UTF-8
# 最小路径和
# 给定一个m*n的数组，数组中包含非负数，从该数组左上角到该数组右下角的最小路径和。（只能向下或者向右移动）。数组格式如下：
# [[1,3,1],
#  [1,5,1],
#  [4,2,1]]
"""
解题思路：
动态规划：
从左上角开始对数组进行遍历，将grid（数组）内容存储为走到当前位置的最短路径和。
故只考虑当前位置的左边和上边哪个小，就选择哪个路径即可
"""

class Solution(object):
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:   # 起始位置
                    continue
                if i==0 and j!=0:      # 向右移动
                    grid[i][j] = grid[i][j-1]+grid[i][j]
                    continue
                if i!=0 and j==0:       # 向下移动
                    grid[i][j] = grid[i-1][j]+grid[i][j]
                    continue
                if i!=0 and j!=0:       # 找到左边和上边的最小值
                    grid[i][j] = min(grid[i-1][j],grid[i][j-1])+grid[i][j]
                    continue
        return grid[m-1][n-1]

nums = [[1,3,1],
        [1,5,1],
        [4,2,1]]
a = Solution()
b = a.minPathSum(nums)
print(b)