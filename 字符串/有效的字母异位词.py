# coding=UTF-8
# 242. 有效的字母异位词
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
# 输入: s = "anagram", t = "nagaram"
# 输出: true
"""
方法1. 使用python中的Counter模块，可以便捷统计两个单词出现的字符及其出现次数     哈希表的便捷方法
方法2. 使用排序来判断
"""
from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return Counter(s) == Counter(t)

m = 'cat'
n = 'tac'
a = Solution()
b = a.isAnagram(m,n)
print(b)