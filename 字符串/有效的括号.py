# 20. 有效的括号
"""
关于栈的应用一般是找最近对应关系这一类的问题，关于队列的问题一般是作为广度优先搜索的辅助数据结构这样。
总之，一般来说，关于栈和队列的应用一般都是作为用于解决其他问题的一种辅助数据结构这样。
"""
class Solution:
    def isValid(self, s):
        d = {'(':')','[':']','{':'}'}
        stack = []  # 使用栈这种数据结构
        for cur in s:
            if cur in d.keys():
                stack.append(cur)
            elif cur in d.values():
                if len(stack) == 0 or d.get(stack[-1]) != cur:  # 分别对应如[]},[}这两种情况
                    return False
                else:
                    stack.pop()
        if len(stack) == 0:
            return True
        else:
            return False
        
        



