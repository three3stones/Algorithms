# coding=UTF-8
# 二叉树层序遍历（按层输出）
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def trav(self,root):
        if not root:
            return root
        res = []        # 总结果
        queue = []      # 辅助数据结构：队列
        queue.append(root)
        while queue:
            l = len(queue)      # 一层的长度
            temp = []           # 临时存储一层的结果，会在每层开始时置空
            while l:
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                temp.append(node.val)
                l -= 1
            res.append(temp)
        return res

if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)
    g = TreeNode(7)
    h = TreeNode(8)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    d.left = h

    test = Solution()
    result = test.trav(a)
    print(result)       # [[1], [2, 3], [4, 5, 6, 7], [8]]

    # """ 输出每层的均值 """
    # import numpy as np
    # g = list(map(lambda x:np.mean(x), result))
    # print(g)            # [1.0, 2.5, 5.5, 8.0]