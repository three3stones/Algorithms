# 二叉搜索树的相关操作

class Solution:
    """
    从根节点开始，若插入的值比根节点的值小，则将其插入根节点的左子树；若比根节点的值大，则将其插入根节点的右子树。
    该操作可使用递归进行实现。
    """
    def insert(self, root, val):
        '''二叉搜索树插入操作'''
        if root == None:
            root = TreeNode(val)
        elif val < root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)
        return root

    """
    从根节点开始查找，待查找的值是否与根节点的值相同，若相同则返回True；
    否则，判断待寻找的值是否比根节点的值小，若是则进入根节点左子树进行查找，否则进入右子树进行查找。该操作使用递归实现。
    """
    def query(self, root, val):
        '''二叉搜索树查询操作'''
        if root == None:
            return False
        if root.val == val:
            return True
        elif val < root.val:
            return self.query(root.left, val)
        elif val > root.val:
            return self.query(root.right, val)

    def findMin(self, root):
        '''查找二叉搜索树中最小值点'''
        if root.left:
            return self.findMin(root.left)
        else:
            return root

    def findMax(self, root):
        '''查找二叉搜索树中最大值点'''
        if root.right:
            return self.findMax(root.right)
        else:
            return root

    """
    对二叉搜索树节点的删除操作分为以下三种情况：
    （1）待删除节点既无左子树也无右子树：直接删除该节点即可
    （2）待删除节点只有左子树或者只有右子树：将其左子树或右子树根节点代替待删除节点
    （3）待删除节点既有左子树也有右子树：找到该节点右子树中最小值节点，使用该节点代替待删除节点，然后在右子树中删除最小值节点。
    """
    def delNode(self, root, val):
        '''删除二叉搜索树中值为val的点'''
        if root == None:
            return 
        if val < root.val:
            root.left = self.delNode(root.left, val)
        elif val > root.val:
            root.right = self.delNode(root.right, val)
        # 当val == root.val时，分为三种情况：只有左子树或者只有右子树、有左右子树、即无左子树又无右子树
        else:
            if root.left and root.right:
                # 既有左子树又有右子树，则需找到右子树中最小值节点
                temp = self.findMin(root.right)
                root.val = temp.val
                # 再把右子树中最小值节点删除
                root.right = self.delNode(root.right, temp.val)
            elif root.right == None and root.left == None:
                # 左右子树都为空
                root = None
            elif root.right == None:
                # 只有左子树
                root = root.left
            elif root.left == None:
                # 只有右子树
                root = root.right
        return root

    """
    实现二叉搜索树的中序遍历，并打印出来。该方法打印出来的数列将是按照递增顺序排列。
    """
    def printTree(self, root):
        # 打印二叉搜索树(中序打印，有序数列)
        if root == None:
            return 
        self.printTree(root.left)
        print(root.val, end = ' ')
        self.printTree(root.right)