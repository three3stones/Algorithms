# 将有序数组转换为二叉搜索树
# 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

# 给定有序数组: [-10,-3,0,5,9],
# 一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
#       0
#      / \
#    -3   9
#    /   /
#  -10  5

"""
思路：
输入数组已有序，相当于是BST的中序遍历，所以只要按照中序遍历的逆过程就可以建立BST了。
中序遍历数组的中间元素 nums[mid] 是root，
左子树是用nums[ :mid]建立的BST，右子树是用nums[mid + 1:]建立的BST。
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        l = len(nums)
        root = TreeNode(nums[l // 2])
        root.left = self.sortedArrayToBST(nums[:l//2])
        root.right = self.sortedArrayToBST(nums[l//2 + 1:])
        return root

if __name__ == "__main__":
    nums = [-10,-3,0,5,9]
    a = Solution()
    b = a.sortedArrayToBST(nums)
    