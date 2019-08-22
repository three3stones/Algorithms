# coding=UTF-8
# 合并二叉树
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTree(self,t1,t2):
        if not t1:
            return t2
        if not t2:
            return t1
        
        t1.val = t1.val + t2.val
        t1.left = self.mergeTree(t1.left, t2.left)
        t1.right = self.mergeTree(t1.right, t2.right)

        return t1

    def inorder(self,root):
        if not root:
            return root
        print(root.val,end=' ')
        self.inorder(root.left)
        self.inorder(root.right)

if __name__ == "__main__":
    p1 = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(3)
    p4 = TreeNode(4)
    p1.left = p2
    p1.right = p3
    p2.left = p4

    q1 = TreeNode(1)
    q2 = TreeNode(2)
    q3 = TreeNode(3)
    q4 = TreeNode(4)
    q1.left = q2
    q1.right = q3
    q3.right = q4

    a = Solution()
    a.inorder(p1)
    print('\t')
    print("-"*20)
    a.inorder(q1)
    print('\t')
    print("-"*20)
    b = a.mergeTree(p1,q1)
    a.inorder(b)