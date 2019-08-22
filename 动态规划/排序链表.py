# coding=UTF-8
# 排序链表
# 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
# 输入: 4->2->1->3 
# 输出: 1->2->3->4

"""
思路: 
这就需要分析一下各个排序算法的复杂度了。时间复杂度在O(nlogN)的排序算法是快速排序，堆排序，归并排序。
但是快排的最坏时间复杂度是O(n^2),平均时间复杂度为O(nlogn)，所以不考虑快速排序。而堆排序太繁琐了,生硬地排除了。
对于数组来说占用的空间复杂度为O(1),O(n),O(n)。但是对于链表来说使用归并排序占用空间为O(1).

投机取巧方法：
第一次遍历链表，将链表中的值顺序存储到列表中，第二次遍历链表，将排序后的列表的值放入链表中，
时间复杂度为O(2n),空间复杂度应该为O(2n)，时间复杂度为O(n)
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

"""
1. 找中点，把链表一分为二
2. 递归处理左右半边
3. 合并排好序的部分
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self,head):
        if head is None or head.next is None:       
            return head
        pre, slow, fast = None, head, head
        # 找到链表的中点
        while fast and fast.next:       # 注意对于偶数个节点，slow最终指向的是第二个中间节点
            pre = slow
            slow = slow.next
            fast = fast.next.next
        
        pre.next = None     # 将链表切断为两部分
        left, right = self.sortList(head), self.sortList(slow)  # 递归终止条件： 当head.next == None时，说明只有一个节点了，直接返回此节点。
        return self.merge(left, right)

    def merge(self,l1,l2):
        if not l1:
            return l2
        if not l2:
            return l1
        
        if l1.val < l2.val:
            head = ListNode(l1.val)
            head.next = self.merge(l1.next, l2)
        else:
            head = ListNode(l2.val)
            head.next = self.merge(l1, l2.next)
        return head

if __name__ == "__main__":
    p = ListNode(4)
    p1 = ListNode(2)
    p2 = ListNode(1)
    p3 = ListNode(3)
    p.next = p1
    p1.next = p2
    p2.next = p3

    a = Solution()
    b = a.sortList(p)
    while b:
        print(b.val)
        b = b.next