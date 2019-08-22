# coding=UTF-8
# 438. 找到字符串中所有字母异位词
# 给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
# 字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
# 输入: s: "cbaebabacd" p: "abc"
# 输出: [0, 6]

"""
1. 关于字母易位词。首先回顾一下字母易位词的判别条件：如果两个字符串中每个字符出现的次数均相同，那么这两个字符串互为字母易位词，例如"aabcc"与"accba"就互为字母易位词。技术实现上，我们可以通过python中collections模块中的Counter函数得到某一个字符串中每个字符出现次数的统计，如果字符串s1和s2的统计结果Counter(s1)==Counter(s2)，那么s1和s2就互为字母易位词。
2. 滑动窗口。这里，我们要在字符串p中找到字符串s的字母易位词，可以在字符串s中构建一个长度与p一致的滑窗，
   从头到尾划过字符串s，在滑动的过程中，我们可以判别滑窗范围内的子串是否是p的字母易位词.
   如果是，则将滑窗左端位置添加到结果列表中。
3. 计数器。我们准备了一个计数器字典，用于记录滑窗中子串各个字符出现次数。
   这里为了减少计算量，我们并非每次都对滑窗进行字符统计，而是只对计数器中新加入的字符和刚删除的字符进行处理。
"""

from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        p_count = Counter(p)                    # 对字符串p中的字符进行计数
        s_count = Counter(s[:len(p)-1])         # 对字符串s中前len(p)个字符进行计数
        ans = []                                # 结果列表，用于保存s中p的易位词出现位置

        for i in range(len(p)-1, len(s)):       # 从p的长度开始遍历到s的长度
            # s[i]从右边进入滑动窗口
            s_count[s[i]] += 1                  # 更新字符计数器s_count中s[i]的出现次数
            cur_idx = i - len(p) + 1            # 滑动窗口左端元素在s中的位置
            cur_char = s[cur_idx]               # 滑动窗口左端元素
            
            # 易位词判别，比较窗口中字符串s[cur_idx:i]和目标字符串p是否互为易位词
            if s_count == p_count:              
                ans.append(cur_idx)             # 如果是，则将滑动窗口左端位置加入到结果列表中
                
            s_count[cur_char] -= 1              # 将滑动窗口左端元素从窗口中弹出，更新字符计数器
            if s_count[cur_char] == 0:          # 如果弹出后计数器中出现次数变为零
                del s_count[cur_char]           # 从计数器中删除该字符
        return ans

a = Solution()
b = a.findAnagrams('abcab','abc')
print(b)