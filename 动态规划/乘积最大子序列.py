# coding=UTF-8
# 乘积最大子序列
# 给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。
# 输入：[2,3,-2,4]　　输出：６　　　解释：子数组 [2,3] 有最大乘积 6。
# 输入：[-2,0,-1]　　 输出：０     解释：结果不能为 2, 因为 [-2,-1] 不是子数组。

"""
思路：
看到求什么什么的连续子序列，一般都是DP，而且DP【i】代表的还是以nums[i]结尾的连续子序列的某种状态。

基础的dpmax用来表示乘积最大的子序列的乘积，
比较特殊的地方在于，因为是算乘积而且没有限定输入的范围，所以需要考虑负数的情况。
所以要额外开一个dpmin表示乘积最小的子序列的乘积。
"""
class solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        dpmax = [0] * l
        dpmin = [0] * l

        dpmax[0] = nums[0]
        dpmin[0] = nums[0]

        for i in range(1,l):
            dpmax[i] = max(nums[i],max(nums[i] * dpmax[i-1], nums[i] * dpmin[i-1]))
            dpmin[i] = min(nums[i],min(nums[i] * dpmax[i-1], nums[i] * dpmin[i-1]))

        return max(dpmax)

if __name__ == "__main__":
    a = solution()
    b = a.maxProduct([2,3,-2,4])
    print(b)