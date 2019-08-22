# 平衡二叉树
# 给定一个二叉树，判断它是否是高度平衡的二叉树。
# 一棵高度平衡二叉树定义为：一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
# 输入：[3,9,20,null,null,15,7]    输出：True
# 输入：[1,2,2,3,3,null,null,4,4]  输出：False

"""
根据题目平衡二叉树的定义，我们只需要保证每一个结点的左右子树均平衡且最大深度差不大于1即可。
这里我们可以使用 "二叉树的最大深度" 来计算每一棵子树的最大深度，通过递归遍历判断各个结点是否平衡：

1. 当输入的根结点为空时，该二叉树平衡；
2. 调用本函数进行递归，当输入结点的左右子树均为平衡二叉树，且最大深度差不大于1时，二叉树平衡；
3. 返回结果。
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        # 获得以root为根结点的树的最大深度
        def maxdepth(root):
            if root is None:
                return 0
            left = maxdepth(root.left)+1
            right = maxdepth(root.right)+1
            return max(left, right)

        # 判定是否为平衡二叉树
        def is_balanced(root):
            if root is None:        # 如果是空树，则一定是平衡二叉树
                return True
            return is_balanced(root.left) and is_balanced(root.right) and abs(maxdepth(root.left) - maxdepth(root.right)) <= 1

        return is_balanced(root)
  

if __name__ == "__main__":
    # 树结构：[1,2,3,4,5,None,None,6]
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    d.left = f

    test = Solution()
    print(test.isBalanced(a)) # Fasle