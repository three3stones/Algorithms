# coding=UTF-8
# 旋转单链表
# 题目：给定一个链表，旋转链表，使得每个节点向右移动k个位置，其中k是一个非负数。
# 如给出链表为 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.

"""
这道题的本质就是，找到 k 位置节点 将其变成尾节点，然后原来链表的尾节点指向原来的头节点
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateList(self, head, n):
        # 排除链表为空，只有一个节点，不旋转的情况
        if head == None or head.next == None or k==0:
            return head
        l = 0
        head1 = head
        while head:
            l += 1
            head = head.next
        k = k % l
        # 排除旋转长度等于链表长度的情况，表示不旋转
        if k == 0:
            return head1
        
        slow = fast = head1
        for i in range(k):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        newhead = slow.next
        slow.next = None
        fast.next = head1
        return newhead


p = ListNode(1)  
p1 = ListNode(2)     
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
b = a.rotateList(p,4)
while b:
    print(b.val)
    b = b.next

