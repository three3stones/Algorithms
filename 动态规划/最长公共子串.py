#　coding=UTF-8
#　最长公共子串
#　要求返回最长的公共子串及其长度

class Solution:
    def find_lcsubstr(self, s1, s2):   
        m=[[0 for i in range(len(s2)+1)]  for j in range(len(s1)+1)]
        mmax=0      #　最长匹配的长度  
        p=0         #　最长匹配对应在s1中的最后一位  
        for i in range(len(s1)):  
            for j in range(len(s2)):  
                if s1[i]==s2[j]:  
                    m[i+1][j+1]=m[i][j]+1  
                    if m[i+1][j+1]>mmax:        # 只要更新最大长度，那么p就加1
                        mmax=m[i+1][j+1]        # p代表了最长公共子串在s1中的最后一位
                        p=i+1  
        return s1[p-mmax:p],mmax   #　返回最长子串及其长度  

a = Solution()
b = a.find_lcsubstr('abcdfg','abdfg')
print(b)