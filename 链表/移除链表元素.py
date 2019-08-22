# 203. 移除链表元素  
# 删除链表中等于给定值 val 的所有节点。

# coding=UTF-8
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head, val):
        new = ListNode(0)  # 在head前创造新节点，用于删除第一个节点
        new.next = head
        pre = new
        while pre.next:
            if pre.next.val == val:
                pre.next = pre.next.next
            else:
                pre = pre.next
        return new.next



p = ListNode(1)     
p1 = ListNode(3)      
p2 = ListNode(3)
p3 = ListNode(4)
p.next = p1
p1.next = p2
p2.next = p3

a = Solution()
b = a.removeElements(p,1)
while b:
    print(b.val)
    b = b.next


