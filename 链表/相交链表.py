# coding=UTF-8
# 相交链表
# 编写一个程序，找到两个单链表相交的起始节点。

# 输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
# 输出：Reference of the node with value = 8
# 输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，
# 链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
# 如果两个链表不相交，返回 null。

"""
方法一：
先求两个链表的长度，然后在让相对长的链表走到跟短链表相同长度的位置，然后再一起遍历，找到相等（位置，地址都相等，这里是个坑）的位置，返回。
若没有找到，返回None。时间复杂度O(n), 空间复杂度O(l)

方法二：
通过巧妙的方法，使两个链表到达相等位置时走过的是相同的距离。
链表1的长度是x1+y，链表2的长度是x2+y，我们同时遍历链表1和链表2，到达末尾时，再指向另一个链表。
则当两链表走到相等的位置时： x1+y+x2 = x2+y+x1
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        l1, l2 = 0,0
        pa, pb = headA, headB
        while pa:
            l1 += 1
            pa = pa.next
        while pb:
            l2 += 1
            pb = pb.next
        
        if l1 > l2:         # 确保l1 < l2
            l1,l2,headA,headB = l2,l1,headB,headA
        
        diff = l2 - l1
        while diff:
            headB = headB.next
            diff -= 1

        while headA:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        return None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        p,q = headA,headB
        while p!=q:
            p = p.next if p else headB
            q = q.next if q else headA
        return p

if __name__ == "__main__":
    p = ListNode(4)  
    p1 = ListNode(1)     
    p2 = ListNode(8)
    p3 = ListNode(4)
    p4 = ListNode(5)   
    p.next = p1
    p1.next = p2
    p2.next = p3
    p3.next = p4
    
    q = ListNode(5)  
    q1 = ListNode(0)     
    q2 = ListNode(1)
    q3 = ListNode(8)
    q4 = ListNode(4)  
    q5 = ListNode(5) 
    q.next = q1
    q1.next = q2
    q2.next = q3
    q3.next = q4
    q4.next = q5

    a = Solution()
    b = a.getIntersectionNode(p,q)

