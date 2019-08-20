# 347. 前K个高频元素
# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]

"""
1. 建立哈希表（字典）存储数字及其出现的次数
2. 根据字典的值逆序排序
3. 拿出前K个元素的key
"""
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {} ; res = []
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        a = sorted(d.items(), key = lambda x:x[1] ,reverse = True)
        for i in a[:k]:
            res.append(i[0])
        return res

x = Solution()
y = x.topKFrequent([1,1,1,2,2,3],2)
print(y)