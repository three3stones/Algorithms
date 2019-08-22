# coding=UTF-8
# 寻找单链表的中间节点
"""
本题使用　快慢指针　思想
慢指针每次移动一步，快指针每次移动两步
（1）链表长度是偶数，快指针下一个节点为NULL，此时慢指针指向节点以及下一个节点为中间节点。 
（2）链表长度是奇数，快指针指向NULL，此时中间结点就是慢指针指向的节点（慢指针先移动，快指针后移动）。
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def midnode(self, head):
        slow = fast = head
        while fast:
            if fast.next == None:
                return slow.val
            elif fast.next.next == None:
                return slow.val, slow.next.val
            else:
                slow = slow.next
                fast = fast.next.next

p = ListNode(1)  #测试代码
p1 = ListNode(2)      #建立链表1->2->3->None
p2 = ListNode(3)
p3 = ListNode(4)
p4 = ListNode(5)
p5 = ListNode(6)
p.next = p1
p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5

a = Solution()
b = a.midnode(p)
print(b)