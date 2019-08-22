# 和为S的两个数字
# 输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。

"""
数列满足递增，设两个头尾两个指针i和j，
若ai + aj == sum，就是答案（相差越远乘积越小）
若ai + aj > sum，aj肯定不是答案之一（前面已得出 i 前面的数已是不可能），j -= 1
若ai + aj < sum，ai肯定不是答案之一（前面已得出 j 后面的数已是不可能），i += 1
"""

class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # 两头开始找匹配，乘积最小必定为最先找到的，如7+8=15 1+14=15乘积1*14小
        low,high = 0, len(array)-1
        while low < high:
            if array[low] + array[high] < tsum:
                low += 1
            elif array[low] + array[high] > tsum:
                high -= 1
            else:
                return [array[low], array[high]]
        return []            # 匹配失败返回空list