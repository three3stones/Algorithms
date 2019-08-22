# 14.最长公共前缀
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。

# coding=UTF-8
class Solution:
    def longestCommonPrefix(self, strs):
        res = ""
        if len(strs) == 0:
            return ""
        for each in zip(*strs): #zip()函数用于将可迭代对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表
            if len(set(each)) == 1: #利用集合判断是否一致
                res += each[0]
            else:
                return res
        return res



strs = ["flower","flow","flight"]
a = Solution()
b = a.longestCommonPrefix(strs)
print(b)



strs = ["flower","flow","flight"]
print(zip(*strs))