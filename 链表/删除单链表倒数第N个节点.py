# coding=UTF-8
# 删除链表中倒数第Ｎ个节点

"""
如果想操作链表的某个节点(添加，删除)还必须知道这个节点的前一个节点。
所以我们删除倒数第 n 个元素就要找到倒数第 n + 1 个元素。
然后将倒数第 n + 1 个元素 p 的 next 指针 p.next 指向 p.next.next 。
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        pre = head
        end = head
        # 使 pre 和 end 相差n个位置，当 end 到达结尾时，pre 刚好指向倒数第n+1个位置
        for i in range(n):
            end = end.next
        # 针对链表正好有n个节点的情况
        if end == None:
            return head.next
        while end.next:
            end = end.next
            pre = pre.next
        pre.next = pre.next.next
        return head

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
b = a.removeNthFromEnd(p,3)
while b:
    print(b.val)
    b = b.next