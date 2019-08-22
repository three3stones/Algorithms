# 有序链表转换二叉搜索树

# 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。   


# 给定的有序链表： [-10, -3, 0, 5, 9],
# 一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：
#       0
#      / \
#    -3   9
#    /   /
#  -10  5

"""
用快慢指针找到链表的中点，然后递归建树。
"""

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        # 寻找链表的中点
        slow, fast = head, head
        pre = head
        while fast and fast.next:        
            pre = slow          # pre 最后指向链表中点的前一个节点
            slow = slow.next    # slow 最后指向链表的中点
            fast = fast.next.next
        pre.next = None
        part1 = head
        part2 = slow.next
        
        # 递归构建二叉搜索树
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(part1)
        root.right = self.sortedListToBST(part2)
        return root
