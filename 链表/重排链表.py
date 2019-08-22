# coding=UTF-8
# 重排链表
# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# 示例 :
# 给定链表 1->2->3->4, 重新排列为 1->4->2->3.
# 给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.

"""
通过给出的例子，可以看出，原链表的前半部分没有改变，后半部分从最后开始依次插入前半部分的间隔中，因此解决这个问题需要分三步。
1. 利用快慢指针，找到原链表的中点
2. 将后半部分链表进行翻转
3. 将反转之后的后半部分链表依次插入前半部分链表的间隔中
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head):
        """ 1. 利用快慢指针，找到原链表的中点  """
        if not head or not head.next:
            return head
        slow ,fast = head, head
        while fast and fast.next:      # 如果链表是奇数个，slow正好指向中间节点；偶数的话，slow指向中间靠右的节点
            slow = slow.next
            fast = fast.next.next

        secondhead = slow.next
        slow.next = None        # 切断链表
        
        """ 2. 反转后面的一半链表，新链表头是newhead  """
        cur = secondhead
        tmp = None
        newhead = None
        while cur:
            tmp = cur.next
            cur.next = newhead
            newhead = cur
            cur = tmp
        
        """ 3. 将反转之后的后半部分链表依次插入前半部分链表的间隔中  """
        l1, l2 = head, newhead
        while l1 and l2:
            cur = l2         # 每次把后半段链表的第一个拿出来
            l2 = l2.next
 
            cur.next = l1.next      # 插到前半段链表里
            l1.next = cur
            l1 = l1.next.next 
 
        return head

            
            
if __name__ == "__main__":
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
    b = a.reorderList(p)
    while b:
        print(b.val)
        b = b.next