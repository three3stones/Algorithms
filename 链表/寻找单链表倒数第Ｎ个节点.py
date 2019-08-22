# coding=UTF-8
# 单链表求倒数第 N 个节点

"""
如果我们让快指针先走 n-1 步后，然后让慢指针出发。
快慢指针每次都只移动一个位置，当快指针移动到链表末尾的时候，慢指针就正处于倒数第 N 个节点的位置呢。
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def findNthFromEnd(self,head,n):
        slow = fast = head
        for i in range(n-1):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        return slow

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
b = a.findNthFromEnd(p,3)
while b:
    print(b.val)
    break