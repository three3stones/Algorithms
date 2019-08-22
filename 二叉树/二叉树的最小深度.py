# coding=UTF-8
# 二叉树的最小深度

"""
1. 迭代法：　算法遍历二叉树每一层，一旦发现某层的某个结点无子树，就返回该层的深度，这个深度就是该二叉树的最小深度
2. 递归法：　用递归解决该题和"二叉树的最大深度"略有不同。
   　　　　　主要区别在于对“结点只存在一棵子树”这种情况的处理，在这种情况下最小深度存在的路径肯定包括该棵子树上的结点
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
        for val in vals_list:
            self.add_node_in_order(val)

    # 方法一：迭代法
    """
    二叉树的最小深度需要从1开始，因为后面的循环是基于一层的节点来说的，只有把当前层的所有节点都遍历完成，
    才会把深度加１
    """
    def mindepth_diedai(self, root):
        if root is None:
            return 0
        else:
            queue = []
            queue.append(root)
            mindepth = 1           
            while queue:
                n = len(queue)
                while n:
                    node = queue.pop(0)
                    n = n-1
                    if node.left is None and node.right is None:
                        return mindepth
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                mindepth += 1
        return mindepth

    # 方法二：递归法
    def mindepth_digui(self, root):
        if root is None:
            return 0
        if not root.left and root.right is not None:
            return self.mindepth_digui(root.right)+1
        if root.left is not None and not root.right:
            return self.mindepth_digui(root.left)+1
        left = self.mindepth_digui(root.left)+1
        right = self.mindepth_digui(root.right)+1
        return min(left,right)



if __name__ == "__main__":
    nodes = [1,2,3,4,None,5,None,None,6]
    print('建立二叉树')
    test1 = BiTree()
    test1.set_up_in_order(nodes)
    print('迭代法的二叉树最小深度：')
    print(test1.mindepth_diedai(test1.root))
    print('递归法的二叉树最小深度：')
    print(test1.mindepth_digui(test1.root))