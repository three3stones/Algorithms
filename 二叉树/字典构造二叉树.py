# coding=UTF-8
# 从字典初始化构造二叉树

""" 
列表顺序构造的二叉树永远都是完全二叉树 
如果想生成一棵不规则的二叉树，应该选择使用字典方法构造二叉树
"""

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

# 字典形式的二叉树
# dict_tree = {
#     "element": 0,
#     "left": {
#         "element": 1,
#         "left": {
#             "element": 3,
#             "left": 6,
#             "right": 7,
#         }
#     },
#     "right": {
#         "element": 2,
#         "left": 4,
#         "right": {
#             "element": 5,
#             "left": 8,
#             "right": 9,
#         },
#     },
# }


"""
字典实现二叉树
"""
class BiTree:
    def set_up_from_dict(self, dict_instance):
        if not isinstance(dict_instance,dict):
            return None
        else:
            dict_queue = list()         # 存储字典队列
            node_queue = list()         # 存储节点队列
            node = BiNode(dict_instance["element"])
            self.root = node
            node_queue.append(node)
            dict_queue.append(dict_instance)
            while len(dict_queue):
                dict_in = dict_queue.pop(0)
                node = node_queue.pop(0)
                # 对于一个节点的子节点，需要判断是否为空、字典、数字
                if isinstance(dict_in.get("left", None), (dict, int, float, str)):
                    if isinstance(dict_in.get("left", None), dict):
                        dict_queue.append(dict_in.get("left", None))
                        left_node = BiNode(dict_in.get("left", None)["element"])
                        node_queue.append(left_node)
                    else:
                        left_node = BiNode(dict_in.get("left", None))
                    node.left = left_node

                if isinstance(dict_in.get("right", None), (dict, int, float, str)):
                    if isinstance(dict_in.get("right", None), dict):
                        dict_queue.append(dict_in.get("right", None))
                        right_node = BiNode(dict_in.get("right", None)["element"])
                        node_queue.append(right_node)
                    else:
                        right_node = BiNode(dict_in.get("right", None))
                    node.right = right_node
    
    def pack_to_dict(self):
        """pack up BiTree to dict form using level traversal"""
        if self.root is None:
            return None
        else:
            node_queue = list()
            dict_queue = list()
            node_queue.append(self.root)
            dict_pack = self.root.dict_form()
            dict_queue.append(dict_pack)
            while len(node_queue):
                q_node = node_queue.pop(0)
                dict_get = dict_queue.pop(0)
                if q_node.left is not None:
                    node_queue.append(q_node.left)
                    dict_get["left"] = q_node.left.dict_form()
                    dict_queue.append(dict_get["left"])
                if q_node.right is not None:
                    node_queue.append(q_node.right)
                    dict_get["right"] = q_node.right.dict_form()
                    dict_queue.append(dict_get["right"])
        return dict_pack


# 测试
test = {
    "element": 0,
    "left": {
        "element": 1,
        "left": {
            "element": 3,
            "left": 6,
            "right": 7,
        }
    },
    "right": {
        "element": 2,
        "left": 4,
        "right": {
            "element": 5,
            "left": 8,
            "right": 9,
        },
    },
}

a = BiTree()
b = a.set_up_from_dict(test)
c = a.pack_to_dict()
print(c)
print(c['left'])
print(c['right'])