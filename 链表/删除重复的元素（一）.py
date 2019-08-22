# 83.删除排序链表中的重复元素 I　  
# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
  
# coding=UTF-8
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode: 
        l = []
        first = head
        pre = None
        while head:
            if head.val not in l:
                l.append(head.val)
                pre = head
                head = head.next
            else:
                pre.next = head.next
                head = head.next
        return first

p = ListNode(1)
p1 = ListNode(2)
p2 = ListNode(3)
p3 = ListNode(2)
p.next = p1
p1.next = p2
p2.next = p3


result = Solution()
a = result.deleteDuplicates2(p)
while a:
    print(a.val)
    a = a.next