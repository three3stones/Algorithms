# coding=UTF-8
# 98.验证是否为二叉搜索树

# 假设一个二叉搜索树具有如下特征：
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
"""
思路：　中序遍历递增 则为搜索二叉树
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 判断中序遍历结果是否严格单调递增
    def isValidBST(self, root):
        if root is None:        # 针对输入是[]的情况，判断为符合标准
            return True
        res = self.inorder(root)
        for i in range(1,len(res)):
            if res[i] <= res[i-1]:
                return False
        return True
    
    # 存储中序遍历的结果
    def inorder(self,root):
        if root is None:
            return None
        res = []
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)        # 存储中序遍历的节点值
            node = node.right
        print(res)
        return res


if __name__ == '__main__':
    a = TreeNode(12)
    b = TreeNode(5)
    c = TreeNode(18)
    d = TreeNode(2)
    f = TreeNode(15)
    g = TreeNode(19)

    a.left = b
    a.right = c
    b.left = d
    c.left = f
    c.right = g

    test = Solution()
    print(test.isValidBST(a))   # True