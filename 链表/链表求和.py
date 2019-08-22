# coding=UTF-8
# 167.链表求和
# 你有两个用链表代表的整数，其中每个节点包含一个数字。数字存储按照在原来整数中相反的顺序，使得第一个数字位于链表的开头。
# 写出一个函数将两个整数相加，用链表形式返回和。
# 示例：给出两个链表 3->1->5->null 和 5->9->2->null，返回 8->0->8->null

"""
函数addLists，入参为两个链表，长度无限制，即可能存在长度：list1 > list2; list1 = list2; list1 < list2;
最终链表长度依据最长链表长度n，返回链表长度（n~n+1）
处理思路:
    链表相加后的值直接在第一个链表上进行修改，最后返回第一个链表的头结点
    在链表末尾之前，执行循环体结构；链表末尾需要考虑是否再进一位（添加一个值为1的节点）
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
 
class Solution:
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2
    def addLists(self, l1, l2):
        if l1 is None: return l2
        if l2 is None: return l1
         
        head1 = l1
        head2 = l2
        flag = 0
        
        while head1.next is not None or head2.next is not None:
            # 存在某一链表next为空时，构造next.val = 0，不影响加法结果
            if head1.next is None:
                head1.next = ListNode(0)
            if head2.next is None:
                head2.next = ListNode(0)
                 
            sumNum = head1.val + head2.val
            if sumNum >= 10:
                head1.val = sumNum % 10
                flag = 1
                head1.next.val += 1
            else:
                head1.val = sumNum
                flag = 0
            head1 = head1.next
            head2 = head2.next
        else:
            # 链表末尾时，单独处理，其和大于10时，追加节点
            head1.val = head1.val + head2.val
            if head1.val >= 10:
                head1.val = head1.val % 10
                head1.next = ListNode(1)
        return l1

list11 = ListNode(2)
list12 = ListNode(1)
list13 = ListNode(6)
list11.next = list12
list12.next = list13

list21 = ListNode(7)
list22 = ListNode(9)
list21.next = list22

a = Solution()
b = a.addLists(list11, list21)
while b:
    print(b.val)
    b = b.next