# coding=UTF-8
# 142.环形链表(二)
# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
# 如果 pos 是 -1，则在该链表中没有环。

"""
判断链表是否有环并找到入环节点:（快慢指针）
1、如果快指针走到空，无环
2、如果二者相遇，有环
3、相遇后，找个新指针返回链表开头，慢指针不动
4、两个指针同时走，每次均走一步，相遇点即为入环点
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None or head.next.next == None:
            return None
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:            # 相遇即为有环
                new = head
                while new != slow:
                    slow = slow.next
                    new = new.next
                return new
        return None
                