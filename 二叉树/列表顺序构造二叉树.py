# coding=UTF-8
# 顺序构造二叉树

""" 列表顺序构造的二叉树永远都是完全二叉树 """

"""
首先声明一个二叉树节点
"""
class BiNode:
    def __init__(self, element=None, left=None, right=None):
        self.element = element
        self.left = left
        self.right = right
    # 返回节点的取值
    def get_element(self):
        return self.element
    # 以字典的形式返回节点
    def dict_form(self):
        dict_set = {
            "element":self.element,
            "left":self.left,
            "right":self.right
        }
        return dict_set
    def __str__(self):
        """当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据"""
        return str('ttt')

"""
实现二叉树
"""
class BiTree:
    def __init__(self, tree_node = None):
        self.root = tree_node
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
                    q_node.right = None
                    break
                else:
                    node_queue.append(q_node.left)
                    node_queue.append(q_node.right)

    def set_up_in_order(self, elements_list):
        """ 通过列表对树进行顺序构造 """
        for elements in elements_list:
            self.add_node_in_order(elements)

