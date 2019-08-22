#########################################　合并两个有序链表　#########################################     
# 合并两个有序链表
class Solution:
    def mergeTwoLists(self, l1, l2):    
        head = ListNode(0)      # 创造一个新链表
        first = head
        # 比较两个链表的值
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        
        if l1 == None:
            head.next = l2
        elif l2 == None:
            head.next = l1
        return first.next

p = ListNode(1)
p1 = ListNode(2)
p2 = ListNode(3)
p.next = p1
p1.next = p2

r = ListNode(1)
r1 = ListNode(5)
r2 = ListNode(9)
r.next = r1
r1.next = r2

a = Solution()
result = a.mergeTwoLists(p, r)
while result:
    print(result.val)
    result = result.next