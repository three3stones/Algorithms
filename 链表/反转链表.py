#########################################　反转链表　#########################################     
# coding=UTF-8
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 迭代思想
def ReverseList(self, pHead):
    if pHead == None or pHead.next == None:
        return pHead  
    cur = pHead 
    tmp = None
    newhead = None 
    # 一共分为四步
    while cur:  
        tmp = cur.next   
        cur.next = newhead  
        newhead = cur
        cur = tmp
    return newhead



# 递归思想
# 如果要倒转的链表有n个节点，那么如果第一个节点后面的n-1个节点已经正确倒转了的话，
# 只要处理第一个和第二个节点的指向关系就可以了。要使后面n-1个节点正确倒转，那么先要使得后面的n-2个节点正确倒转。
# 于是接这么递归下去。最后只剩一个节点的时候，就什么都不用做了，只需要改变其与原来的上一个节点之间的关系就可以了。
def RecurseList(head):
    """
    递归的写法
    递归重要的是你要学会倒着考虑问题
    """
    if not head or head.next == None:  # 递归终止条件（以及排除特殊值问题）
        return head

    else:
        newhead = RecurseList(head.next)  # newhead一直是指向最后一个节点
        head.next.next = head
        head.next = None   # 仅仅在第一个元素时候起作用(递归就是一个栈，后进先出，所以先考虑末尾，最后考虑头) 
    return newhead          #  最终返回原链表的第一个节点，后面使用next方法调用


p = ListNode(1)  #测试代码
p1 = ListNode(2)      #建立链表1->2->3->None
p2 = ListNode(3)
p3 = ListNode(4)
p.next = p1
p1.next = p2
p2.next = p3

# 输出链表 3->2->1->None

# 注意循环方法和递归方法不可以同时运行

# print("循环方法：")
# a = ReverseList(p)
# while a:
#     print(a.val)
#     a = a.next

print("递归方法：")
newhead = None
b = RecurseList(p)
while b:
    print(b.val)
    b = b.next
