# coding=UTF-8
# 49. 字母异位词分组
# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

"""
使用哈希表，key为排序后的字符串，value为排序前的字符串
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if strs is None:
            return
        d = {}
        for i in strs:
            i_list = list(i)
            i_list.sort()
            i_sort = "".join(i_list)
            if i_sort in d:
                d[i_sort].append(i)
            else:
                d[i_sort] = [i]
        return list(d.values())


a = Solution()
b = a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(b)

