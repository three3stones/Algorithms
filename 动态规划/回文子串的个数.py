# coding=UTF-8
# 回文子串的个数
# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
# 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。
# 输入: "abc"     输出: 3     解释: 三个回文子串: "a", "b", "c".
# 输入: "aaa"     输出: 6     说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".

"""
方法一：暴力求解法，即把所有子串找出来，再逐一判断是不是回文串。
方法二：动态规划法，首先认为字符串中每一个元素都是回文子串，有len(s)个，然后在字符串内寻找长度大于１的回文子串，
                (类似最长回文子串的解法)，最后将二者相加即可
"""

class solution:
    def countSubstrings1(self, s):
        size = len(s)
        count = 0
        res = []
        for i in range(size):
            for j in range(1, size-i+1):
                temp = s[i:i+j]         # 保证后面的索引比前面的大
                if temp == temp[::-1]:
                    count += 1
                    res.append(temp)

        return count,res
    
    def countSubstrings2(self,s):
        size = len(s)
        dp = [[False for _ in range(size)] for _ in range(size)]
        count = 0

        for r in range(1,size):
            for l in range(r):
                if s[l] == s[r] and (r-l <= 2 or dp[l+1][r-1]):
                    dp[l][r] = True
                    count += 1

        return count + size



if __name__ == "__main__":
    a = solution()
    b1 = a.countSubstrings1('tabba')
    b2 = a.countSubstrings2('tabba')
    print(b1)       # 　['t', 'a', 'abba', 'b', 'bb', 'b', 'a']
    print(b2)
