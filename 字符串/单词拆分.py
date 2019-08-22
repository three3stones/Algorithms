# coding=UTF-8

class Solution(object):
    def wordBreak(self, s, wordDict):
        if not s:
            return True
        bp = [0]
        for i in range(len(s)+1):
            #print('当前i:'+str(i))
            for j in bp:
                #print('当前j:'+str(j))
                if s[j:i] in wordDict:
                    #print((j,i))
                    bp.append(i)
                    break
        return bp[-1] == len(s)



a = Solution()
b = a.wordBreak('tomandjerrytom',['tom','jerry','and'])
print(b)

# 最终bp = [0,3,6,11,14]