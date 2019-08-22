# coding=UTF-8
# 86. 分隔链表
# 题目 ： 按某个给定值将链表划分为左边小于这个值，右边大于这个值的新链表 
# 如一个链表 为 1 -> 4 -> 5 -> 2 给定一个数 3 则划分后的链表为 1-> 2 -> 4 -> 5

"""
遍历一遍链表，就可以完成
首先新建两个链表，如果遍历过程中，节点值比给定值小则划在左链表中，反之放在右链表中。遍历完成后拼接两个链表就好。
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def divideList(self,head,num):
        head1 = ListNode(None)
        head11 = head111 = head1
        head2 = ListNode(None)
        head22 = head2
        while head:
            if head.val < num:
                head1.next = ListNode(head.val)
                head1 = head1.next
            else:
                head2.next = ListNode(head.val)
                head2 = head2.next
            head = head.next
        while head11.next:
            head11 = head11.next
        head11.next = head22.next
        return head111.next

p = ListNode(1)  
p1 = ListNode(8)     
p2 = ListNode(4)
p3 = ListNode(7)
p4 = ListNode(2)
p5 = ListNode(6)
p.next = p1
p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5

a = Solution()
b = a.divideList(p, 5)
while b:
    print(b.val)
    b = b.next