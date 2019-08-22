# coding=UTF-8
# 141.环形链表
# 给定一个链表，判断链表中是否有环。
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
# 如果 pos 是 -1，则在该链表中没有环。

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head   # 快慢指针
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:        # 可以证明：如果链表有环，那么快慢指针必定会相遇
                return True
        return False