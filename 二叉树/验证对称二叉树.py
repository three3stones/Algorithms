# coding=UTF-8
# 对称二叉树
"""
方法一：递归
方法二：迭代（队列辅助）
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
 
class Solution(object):
    """
    1. 对根节点进行非空判断，将根节点的左右子树放在一个队列中；
    2. 每次成对取出节点，这两个节点其实是二叉树的对称位置，判断这两个节点的相等情况：
        （1）如果两结点均为空，则继续下一轮循环；
        （2）如果两结点只有一个是空，直接返回Fasle；
        （3）如果两结点都不为空，且它们的数值不同，也直接返回False；
        （4）此时两结点的数值一定相等，将它们的左右子结点逆序加入到队列中，保证每一对结点都是对称的位置。
    3. 如果到最后，队列中为空，则二叉树对称，返回True。

    """
    def isSymmetric_diedai(self, root):
        if root is None:
            return True
        node_queue = [root.left, root.right]        # 在空队列中加入左子树和右子树
        while node_queue:
            left = node_queue.pop(0)                # 依次弹出两个元素
            right = node_queue.pop(0)

            if not right and not left:              # 如果均为空，继续下一个循环
                continue
            if not right or not left:               # 如果只有一个为空，返回False
                return False
            if left.val != right.val:               # 都非空，再判断值是否相等
                return False
            
            # 此处特别要注意append的顺序
            node_queue.append(left.left)            # 将两个左右子树的左右子树逆序加入队列
            node_queue.append(right.right)
            node_queue.append(left.right)
            node_queue.append(right.left)
        
        return True
    

    """
    对称的树的左子树和右子树满足以下条件：

    1. 如果左子树或右子树均为空，则该树对称；

    2. 如果左子树或右子树只有一个为空，则该树不对称；

    3. 如果左子树和右子树均不为空，当左子树的左子树和右子树的右子树镜像对称，且左子树的右子树和右子树的左子树镜像对称时，该树对称。
    """
    def isSymmetric_digui(self,root):
        def isMirror(p,q):              # 判断左右子树是否镜像对称
            if not p and not q:
                return True
            elif not p and q   or   not q and p:
                return False
            else:
                return p.val == q.val and isMirror(p.left, q.right) and isMirror(p.right, q.left)
        return isMirror(root, root)



if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(2)
    d = TreeNode(3)
    e = TreeNode(4)
    f = TreeNode(4)
    g = TreeNode(3)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g

    test = Solution()
    print(test.isSymmetric_digui(a))   # True
                