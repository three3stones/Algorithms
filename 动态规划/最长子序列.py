#!/usr/bin/python3
# coding=UTF-8
# 最长公共子序列

# 子串要求字符必须是连续的，但是子序列就不是这样。最长公共子序列是一个十分实用的问题，
# 它可以描述两段文字之间的“相似度”，即它们的雷同程度，从而能够用来辨别抄袭。
# 对一段文字进行修改之后，计算改动前后文字的最长公共子序列，将除此子序列外的部分提取出来，这种方法判断修改的部分，往往十分准确。
"""
解法就是用动态规划的思想，一个矩阵记录两个字符串中匹配情况。
若是匹配则为左上方的值加1，否则为左方和上方的最大值。一个矩阵记录转移方向，然后根据转移方向，回溯找到最长子序列。
"""
    
class Solution:
    def find_lcsubstr(self, s1, s2):   
        m=[[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]
        for i in range(len(s1)):  
            for j in range(len(s2)):  
                if s1[i] == s2[j]:  
                    m[i+1][j+1] = m[i][j]+1  
                else:
                    m[i+1][j+1] = max(m[i+1][j], m[i][j+1])
        return m[len(s1)][len(s2)]

a = Solution()
b = a.find_lcsubstr('abdfg','abcdfg')
print(b)