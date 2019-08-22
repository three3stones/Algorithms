# coding=UTF-8
# 24. 两两交换链表中的节点
# 你的算法只能使用常数的额外空间，即不能新建链表；
# 并且不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

"""
创建三个指针：

　　head指向开始交换的节点的上一个节点

　　n1指向需要交换的第一个节点，即head.next

　　n2指向需要交换的第二个节点，即head.next.next

循环链表，通过head不断交换n1/n2位置即可。
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swap(self, head):
        # 新建一个节点指向头部
        p = ListNode(None)
        p.next = head
        # 将head更新
        head = p
        while head.next and head.next.next:
            n1 = head.next
            n2 = head.next.next
            # 交换n1和n2
            head.next = n2
            n1.next = n2.next
            n2.next = n1
            head = n1
        return p.next

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
b = a.swap(p)
while b:
    print(b.val)
    b = b.next