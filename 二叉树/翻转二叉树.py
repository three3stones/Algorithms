# 翻转二叉树
# 翻转一棵二叉树。
# 示例：
# 输入：
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9

# 输出：
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
 
class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return root
        temp = root.left        # 中间变量过渡
        root.left = root.right
        root.right = temp
         
        self.invertTree(root.left)
        self.invertTree(root.right)
         
        return root