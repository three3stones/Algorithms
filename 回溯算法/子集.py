# coding=UTF-8
# 78. 子集
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 说明：解集不能包含重复的子集。

# 输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

"""
方法一：　回溯法
方法二：　python库函数　itertools.combinations
        itertools模块combinations(iterable, r)方法可以创建一个迭代器，返回iterable中所有长度为r的子序列，
        返回的子序列中的项按输入iterable中的顺序排序。
"""

class Solution1:
    def subset1(self, nums):
        if not nums:
            return []
        res = []
        n = len(nums)

        def helper(idx, temp_list):
            res.append(temp_list)
            for i in range(idx,n):
                helper(i+1, temp_list+[nums[i]])

        helper(0, [])
        return res


class Solution2:
    def subset2(self, nums):
        import itertools
        res = []
        for i in range(len(nums)+1):
            for tmp in itertools.combinations(nums, i):
                res.append(list(tmp))
        return res

num = [1,2,3]
a1 = Solution1()
a2 = Solution2()
b1 = a1.subset1(num)
b2 = a2.subset2(num)
print(b1)
print(b2)
# [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
# [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
