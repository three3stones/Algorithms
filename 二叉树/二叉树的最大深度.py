# coding=UTF-8
# 二叉树的最大深度
"""
1. 迭代法：从上到下按层级遍历二叉树，有多少层即二叉树有多深（即为求二叉树的深度）
2. 递归法：比较每一条路径的长短
"""
class BiNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class BiTree:
    def __init__(self):
        self.root = None
    # 添加节点
    """
    判断根结点是否存在，如果不存在则插入根结点。否则从根结点开始，判断左子结点是否存在，如果不存在插入, 
    如果左子结点存在判断右结点，不存在插入。如果左右结点存在，再依次遍历左右子结点的子结点，直到插入成功。
    """
    def add_node_in_order(self, element):
        node = BiNode(element)
        if self.root is None:
            self.root = node
        else:
            # 需要一个队列对子结点进行入队与出队。在python上这很简单，一个list 就实现了
            node_queue = list()
            node_queue.append(self.root)
            while len(node_queue):
                q_node = node_queue.pop(0)        # 从列表头部读取
                if q_node.left is None:
                    q_node.left = node
                    break
                elif q_node.right is None:
                    q_node.right = node
                    break
                else:
                    node_queue.append(q_node.left)
                    node_queue.append(q_node.right)

    def set_up_in_order(self, vals_list):
        """ 通过列表对树进行顺序构造 """
        for val in vals_list:
            self.add_node_in_order(val)
    
    # 方法一：迭代法　（其实就是求二叉树的深度）
    def maxdepth_diedai(self, root):
        if root is None:
            return 0
        else:
            queue = []
            queue.append(root)
            maxdepth = 0
            while queue:
                n = len(queue)
                while n:
                    node = queue.pop(0)
                    n = n-1
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                maxdepth += 1
        return maxdepth

    # 方法二：递归法
    def maxdepth_digui(self, root):
        if root is None:
            return 0
        left = self.maxdepth_digui(root.left) + 1       # 其实　self.maxdepth_digui(root.left)　表示一个数字
        right = self.maxdepth_digui(root.right) + 1
        return max(left,right)


if __name__ == "__main__":
    nodes = [1,2,3,4,None,5,None,None,6]
    print('建立二叉树')
    test1 = BiTree()
    test1.set_up_in_order(nodes)
    print('迭代法的二叉树最大深度：')
    print(test1.maxdepth_diedai(test1.root))
    print('递归法的二叉树最大深度：')
    print(test1.maxdepth_digui(test1.root))