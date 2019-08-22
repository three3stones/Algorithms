# coding=UTF-8
# 3. 无重复最长子串
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串的长度。
# 输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

"""
首先逻辑理清楚，u是不重复的字符串，初始化为空字符串，res是我们要返回的结果，初始化为0。

1.for循环次数为s字符串长度，每次循环的字符串用k表示。

2.如果k不在u里面，把k加到u里面，res等于u的长度和res中的最大值。

3.如果k在u里面，说明已经出现重复的字符，这个时候k是一个和u中有重复的字符，index是找出k字符在u中的索引位置，
    将 u 更新为  u=u[index+1:]+k
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        u = ''
        for i in range(len(s)):
            k = s[i]
            if k not in u:
                u+=k
                res = max(len(u),res)
            else:
                index = u.find(k)
                u = u[index+1:]+k
        return res


a = Solution()
b = a.lengthOfLongestSubstring("   ")
print(b)