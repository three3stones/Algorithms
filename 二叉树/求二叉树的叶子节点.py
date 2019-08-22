# 求二叉树的叶子节点
"""
求二叉树的叶子节点使用广度搜索优先，即如果当前节点存在左右子树将左右子树入队。
如果当前节点不存在子树，则该节点为叶节点。继续出队访问下一个节点。直至队列为空。
"""
class BiNode(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BiTree:
    def __init__(self):
        self.root = None

    def add_node_in_order(self, element):
        node = BiNode(element)

        if self.root is None:
            self.root = node
        else:
            node_queue = list()
            node_queue.append(self.root)
            while len(node_queue):
                q_node = node_queue.pop(0)
                if q_node.left is None:
                    q_node.left = node
                    break
                elif q_node.right is None:
                    q_node.right = node
                    break
                else:
                    node_queue.append(q_node.left)
                    node_queue.append(q_node.right)

    def set_up_in_order(self, elements_list):
        for elements in elements_list:
            self.add_node_in_order(elements)

    def leaves(self):
        if self.root is None:
            return 0
        else:
            nums = 0
            queue = []
            queue.append(self.root)
            while queue:
                node = queue.pop(0)
                if node.left is None and node.right is None:
                    # print(node.val)            # 打印叶子结点        
                    nums += 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return nums                             # 输出叶子节点的个数


# 测试
node_list = [1,2,3,4,5,6,7,8,9]
test = BiTree()
test.set_up_in_order(node_list)
print(test.leaves())