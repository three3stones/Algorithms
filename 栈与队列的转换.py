# 两个栈实现队列
"""
第一个栈临时保存插入的数据，当调用弹出函数的时候，如果stack2不为空则直接弹出；为空则把stack1中的数据全部弹出放到stack2中。
"""
class QueueWithTwoStacks:
    def __init__(self):
        self._stack1 = []
        self._stack2 = []
    
    def push(self, num):
        self._stack1.append(num)
    
    def pop(self):
        if self._stack2:
            return self._stack2.pop()
        else:
            while self._stack1:
                self._stack2.append(self._stack1.pop())
            return self._stack2.pop()

if __name__ == "__main__":
    a = QueueWithTwoStacks()
    a.push(1)
    a.push(2)
    a.push(3)
    print(a.pop())  # 1
    print(a.pop())  # 2


# 两个队列实现栈
"""
进栈：元素入队列A
出栈：判断如果队列A只有一个元素，直接出队。否则，把队A中艺术顺序出队并入队B，直到队A中只有一个元素，再直接出队，

为了下一次继续操作，互换队A和队B，弹出队B中的唯一元素。
"""
class StackWithTwoQueues:
    def __init__(self):
        self.queueA = []
        self.queueB = []
    
    def push(self,node):
        self.queueA.append(node)
    
    def pop(self):
        if len(self.queueA)==0:
            return None
        while len(self.queueA)!=1:
            self.queueB.append(self.queueA.pop(0))
        
        self.queueA,self.queueB=self.queueB,self.queueA     # 交换队列 A,B的位置，为了下一次的pop
        return self.queueB.pop()

if __name__ == "__main__":
    b = StackWithTwoQueues()
    b.push(1)
    b.push(2)
    b.push(3)
    print(b.pop())  # 3
    print(b.pop())  # 2