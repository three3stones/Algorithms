# 876. 链表的中间结点
# 给定一个带有头结点 head 的非空单链表，返回链表的中间结点。
# 如果有两个中间结点，则返回第二个中间结点。

# coding=UTF-8
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head):
        count = 0
        pre = head
        index = 0
        while head:
            count += 1
            head = head.next

        if (count % 2) == 0:
            index = (count/2) + 1
        else:
            index = (count + 1) / 2
        
        for i in range(index-1):
            pre = pre.next
        return pre

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
result = a.middleNode(p)
print(result.val)