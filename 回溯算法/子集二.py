# coding=UTF-8
# 90. 子集 II
# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 说明：解集不能包含重复的子集。

# 输入: [1,2,2]
# 输出:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

"""
方法一：　回溯法
方法二：　python库函数　itertools.combinations
        itertools模块combinations(iterable, r)方法可以创建一个迭代器，返回iterable中所有长度为r的子序列，
        返回的子序列中的项按输入iterable中的顺序排序。
"""

class Solution1:
    def subsetsWithDup1(self, nums):
        res = []
        n = len(nums)
        
        def helper(i, tmp):
            tmp = sorted(tmp)
            if tmp not in res:
                res.append(tmp)
            for j in range(i, n):
                helper(j + 1,tmp + [nums[j]])
        
        helper(0, [])
        return res



class Solution2:
    def subsetsWithDup2(self, nums):
        import itertools
        res = []
        for i in range(len(nums)+1):
            for tmp in itertools.combinations(nums, i):
                res.append(list(tmp))    # res是一个二维list
        result = list(set([tuple(t) for t in res]))  # list不可哈希但是tuple可哈希
        result1 = list([list(t) for t in result])   # 最后将tuple转成list
        return result1

a1 = Solution1()
b1 = a1.subsetsWithDup1([1,2,2])
a2 = Solution2()
b2 = a2.subsetsWithDup2([1,2,2])
print(b1)
print(b2)
# [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
# [[1, 2], [1], [1, 2, 2], [2], [], [2, 2]]
 