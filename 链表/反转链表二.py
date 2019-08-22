# coding=UTF-8
# 92.反转链表二
# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。 1 ≤ m ≤ n ≤ 链表长度。
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL

"""
0.保存头节点
1.找到反转部分的前一个节点，保存为start
2.翻转第m到n位链表，记录第m个节点为node_m，第n个节点为node_n，第n+1个节点为end
3.连接链表，start.next = node_n, node_m.next = end
4.返回头节点
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        if not head or not head.next or m == n:
            return head
        dummy = ListNode(None)
        dummy.next = head    # 避免了 m = 1 时的复杂情况
        # 找到反转前一个节点
        start = dummy
        for i in range(m-1):
            start = start.next
        # 需要反转部分的开始节点
        end = cur = start.next
        newhead = None
        # 开始反转
        for i in range(n-m+1):
            tmp = cur.next
            cur.next = newhead
            newhead = cur
            cur = tmp
        # 将三部分链接起来
        start.next = newhead
        end.next = cur
        return dummy.next

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
b = a.reverseBetween(p,3,5)
while b:
    print(b.val)
    b = b.next