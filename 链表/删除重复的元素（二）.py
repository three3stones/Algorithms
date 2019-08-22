# 82.删除排序链表中的重复元素 II 
# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
# coding=UTF-8
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def deleteDuplicates2(self,head):
        '''
        :param head:ListNode 
        :return: ListNode
        '''
        tmp_list = []       # 顺序表
        tmp_dict = {}       # 哈希表
        new1 = ListNode(0)
        new2 = new1
        while head:
            if head.val not in tmp_list:
                tmp_list.append(head.val)
                tmp_dict[head.val] = 1
            else:
                tmp_dict[head.val] += 1 
            head = head.next
        
        # 寻找只出现一次的值，并建立新节点
        for i in tmp_list:
            if tmp_dict[i] == 1:
                new_node = ListNode(i)
                new1.next = new_node
                new1 = new1.next
        return new2.next

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






