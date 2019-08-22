# coding=UTF-8

"""
实现二叉树
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


    # 二叉树的遍历（递归和非递归版本）
    """
    遍历方式的命名，源于其访问节点的顺序。最简单的划分：深度优先，广度优先。 
    深度优先遍历又可分为，前序遍历（pre-order）, 中序遍历（in-order），后序遍历(post-order) 
    对于广度优先而言，遍历没有前序中序后序之分：给定一组已排序的子节点，其“广度优先”的遍历只有一种唯一的结果。 
    二叉树的递归算法相对简单，非递归算法实现要用到辅助栈，算法设计非常巧妙。 
    """

    # 前序遍历（根——左——右）
    ### 递归版本 ###
    def preorder_digui(self,root):
        if root is None:
            return
        print(root.val)
        self.preorder_digui(root.left)
        self.preorder_digui(root.right)

    ### 非递归版本 ###
    """
    preOrder每次都将遇到的节点压入栈，当左子树遍历完毕后才从栈中弹出最后一个访问的节点，再访问其右子树。
    """
    def preorder(self):
        if self.root is None:
            return None
        mystack = []
        node = self.root
        while mystack or node:
            while node:
                # 从根节点开始，一直找它的左子树
                mystack.append(node)
                print(node.val)
                node = node.left
            # while结束表示当前节点node为空，即前一个节点没有左子树了
            # 开始查看它的右子树
            node = mystack.pop()
            node = node.right


    # 中序遍历（左——根——右）
    ### 递归版本 ###
    def inorder_digui(self,root):
        if root is None:
            return
        self.inorder_digui(root.left)
        print(root.val)
        self.inorder_digui(root.right)

    ### 非递归版本 ###
    """
    中序的非递归遍历与先序的非递归遍历类似。先序遍历是先访问节点，然后再将节点入栈，后中序遍历则是先入栈，然后节点弹出栈后再访问。
    """
    def inorder(self):
        if self.root is None:
            return None
        mystack = []
        node = self.root
        while mystack or node:
            while node:
                # 从根节点开始，一直找它的左子树
                mystack.append(node)
                node = node.left
            # while结束表示当前节点node为空，即前一个节点没有左子树了
            # 开始查看它的右子树
            node = mystack.pop()
            print(node.val)
            node = node.right


    # 后序遍历（左——右——根）
    ### 递归版本 ###
    def postorder_digui(self,root):
        if root is None:
            return
        self.postorder_digui(root.left)
        self.postorder_digui(root.right)
        print(root.val)

    ### 非递归版本 ###
    """
    先左，再右，最后才中间节点；访问左子树后，需要跳转到右子树，右子树访问完毕了再回溯至根节点并访问之。
    """
    def postorder(self):
        if self.root is None:
            return 
        stack1 = []
        stack2 = []
        stack1.append(self.root)
        # 这个while循环，用于找到后续遍历的逆序，存在stack2中
        while stack1:
            node = stack1.pop()
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
            stack2.append(node)
        
        while stack2:
            print(stack2.pop().val)


    """
    广度优先遍历与深度优先遍历的区别在于：广度优先遍历是以层为顺序，将某一层上的所有节点都搜索到了之后才向下一层搜索；
    而深度优先遍历是将某一条枝桠上的所有节点都搜索到了之后，才转向搜索另一条枝桠上的所有节点。
    """
    # 层序遍历
    def bfs(self):
        if self.root is None:
            return
        queue = []
        queue.append(self.root)
        while queue:
            node = queue.pop(0)
            print(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

if __name__ == "__main__":
    nodes = [1,2,3,4,5,6,7,8,9]
    test1 = BiTree()
    print('建树：')
    test1.set_up_in_order(nodes)       # 列表顺序导入二叉树
    print('前序递归：')
    test1.preorder_digui(test1.root)   # 1 2 4 8 9 5 3 6 7
    print('前序非递归：')
    test1.preorder()                   # 1 2 4 8 9 5 3 6 7
    print('中序递归：')
    test1.inorder_digui(test1.root)    # 8 4 9 2 5 1 6 3 7
    print('中序非递归：')
    test1.inorder()                    # 8 4 9 2 5 1 6 3 7
    print('后序递归')
    test1.postorder_digui(test1.root)  # 8 9 4 5 2 6 7 3 1
    print('后序非递归')
    test1.postorder()                  # 8 9 4 5 2 6 7 3 1
    print('层序遍历')
    test1.bfs()                        # 1 2 3 4 5 6 7 8 9