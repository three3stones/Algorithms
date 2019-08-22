# coding=UTF-8
# 二叉树的堂兄弟节点

# 在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。
# 如果二叉树的两个节点深度相同，但父节点不同，则它们是一对堂兄弟节点。
# 我们给出了具有唯一值的二叉树的根节点 root，以及树中两个不同节点的值 x 和 y。
# 只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true。否则，返回 false。
# 二叉树中的每一个节点的取值都是唯一的

"""
方法：标记父节点与深度
思路：
当且仅当一对节点深度相同而父节点不相同时，它们是堂兄弟节点。一种非常直接的方法就是通过某种方法求出每一个节点的深度与父节点。

我们用深度优先搜索标记每一个节点，对于每一个节点 node，它的父亲为 par，深度为 d
我们将其记录到 Hashmap 中：parent[node.val] = par 且 depth[node.val] = d。
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isCousions(self, root, x, y):
        parent = {}     # 标记父节点
        depth = {}      # 标记深度
        def dfs(node, par=None):
            if node:
                if par is None:
                    depth[node.val] = 0
                else:
                    depth[node.val] = 1+depth[par.val]
                parent[node.val] = par
                
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)

        return depth[x] == depth[y] and parent[x] != parent[y]

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

    test1 = Solution()
    print(test1.isCousions(a,4,7))  # True

    test2 = Solution()
    print(test2.isCousions(a,8,4))  # False