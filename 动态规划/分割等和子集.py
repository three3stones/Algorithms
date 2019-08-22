# 分割等和子集
# 给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
# 注意:
# 每个数组中的元素不会超过 100    数组的大小不会超过 200
# 输入: [1, 5, 11, 5]   输出: true    解释: 数组可以分割成 [1, 5, 5] 和 [11]
# 输入: [1, 2, 3, 5]    输出: false   解释: 数组不能分割成两个元素和相等的子集.

"""
解析：可以看成一个背包大小为sum/2的 0-1 背包问题。
翻译：给定一个只包含正整数的非空数组。
     是否可以从这个数组中挑选出一些正整数，每个数只能用一次，使得这些数的和等于整个数组元素的和的一半。

dp[i][j] ：表示从数组的 [0, i] 这个子区间内挑选一些正整数，每个数只能用一次，使得这些数的和等于 j。

新来一个数，例如是 nums[i]，根据这个数可能选择也可能不被选择：
如果不选择 nums[i]，在 [0, i - 1] 这个子区间内已经有一部分元素，使得它们的和为 j ，那么 dp[i][j] = true；
如果选择 nums[i]，在 [0, i - 1] 这个子区间内就得找到一部分元素，使得它们的和为 j - nums[i]
以上二者成立一条都行。于是得到状态转移方程是：dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]], (nums[i] <= j)
"""
class solution:
    def canPartition(self, nums):
        size = len(nums)
        # 特判，如果整个数组的和都不是偶数，就无法平分
        if sum(nums) & 1 == 1:
            return False
        
        # 二维dp问题
        target = sum(nums) // 2
        dp = [[False for _ in range(target + 1)] for _ in range(size)]
        
        # 先写第 1 行：第一行的只有取值为nums[0]的位置才是True　　（根据dp[i][j]的定义）
        for i in range(target + 1):
            if nums[0] != i:
                dp[0][i] = False 
            else:
                dp[0][i] = True
       
        # i 表示物品索引
        for i in range(1, size):
            # j 表示容量
            for j in range(target + 1):
                if j >= nums[i]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][-1],dp


if __name__ == "__main__":
    a = solution()
    b = a.canPartition([1, 5, 5, 11])
    print(b)



