# 堆排序
"""
数据结构：堆
堆可以视为一棵完全的二叉树，完全二叉树的一个“优秀”的性质是，除了最底层之外，每一层都是满的。这使得堆可以利用数组来表示，每一个结点对应数组中的一个元素。
完全二叉树可以用列表【顺序存储方式】来存储，通过规律可以从父亲找到孩子或从孩子找到父亲。
父亲节点以 i 表示
　　　　父节点与左孩子节点 下标关系：l = 2i+1
　　　　父节点与右孩子节点 下标关系：r = 2i+2

二叉堆一般分为两种：大根堆(大顶堆)和小根堆(小顶堆)。
　　大根堆：一棵完全二叉树，满足任一节点都比其孩子节点大；
　　　　    特点：最大元素出现在根节点上，处于最大堆的根节点的元素一定是这个堆中的最大值。
　　小根堆：一棵完全二叉树，满足任一节点都比其孩子节点小；
　　　　    特点：最小元素出现在根节点上，处于最小堆的根节点的元素一定是这个堆中的最小值。

核心思想：
　　将待排序的序列构造成一个大顶堆；此时，整个序列的最大值就是堆的根节点。将它与堆数组的末尾元素交换，然后将剩余的n-1个序列重新构造成一个大顶堆。
　　剩余部分调整为大顶堆后,再次将堆顶的最大数取出,再将剩余部分调整为大顶堆。反复执行前面的操作，这个过程持续到剩余数只有一个时结束，最后获得一个有序序列。
堆排序过程：
　　1、建立堆，挨个出数
　　2、得到堆顶元素，为最大元素
　　3、去掉堆顶，将堆最后一个元素放到堆顶，此时可通过一次调整重新使堆有序。
　　4、堆顶元素为第二大元素。
　　5、重复步骤3，直到堆变空。

性能评价：
堆排序对原始记录的排序状态不敏感，因此它无论最好、最坏和平均时间复杂度都是O(nlogn)。
在性能上要好于冒泡、简单选择和直接插入算法。空间复杂度上，只需要一个用于交换的暂存单元。
但是由于记录的比较和交换是跳跃式的，因此，堆排序也是一种不稳定的排序方法。此外，由于初始构建堆的比较次数较多，堆排序不适合序列个数较少的排序工作。
"""

# 大顶堆排序        列表原地修改
class Solution:
    def max_heap_sort(self,data):
        size = len(data)
        high = size - 1     # 最后一个元素的索引
        mid = size >> 1     # 相当于length//2 -1，代表最后一个非叶子节点的索引位置，从这个节点开始，一直往上比较

        # 建堆 从最后一个非叶子节点的子树【最后一个叶子节点与其父节点比较】 开始构建
        while mid >= 0:
            self.adjust_heap(data,mid,high)
            mid -= 1
        
        # 挨个出数
        while high > 0:
            data[0], data[high] = data[high], data[0]      #　把堆顶和堆尾位置交换(省空间，仅在当前列表操作)
            # print(data)
            self.adjust_heap(data,0,high-1)     # 出数的过程破坏了堆，因此要从 0 的位置重新构造大顶堆，并且更新最后一个元素的索引
            high -= 1
        
        return data

    """ 调整父节点与孩子大小， 制作大顶堆 """
    def adjust_heap(self,data,par_node,high):
        """
        调整函数
        data: 列表
        par_node：待调整的子树的根位置
        high：待调整的子树的最后一个节点的位置
        """
        left = 2 * par_node + 1     # 取根节点的左孩子

        while left <= high:     # 如果 left = high 说明没有右孩子，high就是左孩子
            if left != high and data[left] < data[left+1]:
                left += 1                   # 一个根节点下，如果有两个孩子，将 j  指向值大的那个孩子
            
            if data[left] > data[par_node]:     # 如果子节点值大于父节点，就互相交换
                data[left], data[par_node] = data[par_node], data[left]
                par_node = left                 # 将当前节点，作为父节点，检查他的子树是否符合大顶堆
                left = 2 * par_node + 1
            else:
                # 因为调整是从上到下，所以下面的所有子树肯定是排序好了的，
                # 如果调整的父节点依然比下面最大的子节点大，就直接打断循环，堆已经调整好了的
                break

if __name__ == "__main__":
    list1 = [4, 7, 0, 9, 1, 5, 3, 3, 2, 6]
    a = Solution()
    b = a.max_heap_sort(list1)
    print(b)        # [0, 1, 2, 3, 3, 4, 5, 6, 7, 9]
# 大顶堆过程
# [1, 7, 5, 4, 6, 0, 3, 3, 2, 9]
# [2, 6, 5, 4, 1, 0, 3, 3, 7, 9]
# [2, 4, 5, 3, 1, 0, 3, 6, 7, 9]
# [2, 4, 3, 3, 1, 0, 5, 6, 7, 9]
# [0, 3, 3, 2, 1, 4, 5, 6, 7, 9]
# [1, 2, 3, 0, 3, 4, 5, 6, 7, 9]
# [0, 2, 1, 3, 3, 4, 5, 6, 7, 9]
# [1, 0, 2, 3, 3, 4, 5, 6, 7, 9]
# [0, 1, 2, 3, 3, 4, 5, 6, 7, 9]


# 小顶堆排序        新建一个列表
class Solution1:
    def __init__(self):
        self.res = []       # 初始化一个列表，用来接受小顶堆弹出的最小值
    
    def min_heap_sort(self,data):
        size = len(data)
        high = size - 1
        mid = size >> 1
        while mid >= 0:
            self.adjust_heap(data,mid,high)
            mid -= 1

        while len(data) != 0:
            self.res.append(data.pop(0))        # 接受小顶堆弹出的最小值
            # print(self.res)
            self.min_heap_sort(data)            # 对剩下的数据重新进行小顶堆排序

        return self.res

    def adjust_heap(self,data,par_node,high):
        left = par_node * 2 + 1
        
        while left <= high:
            if left != high and data[left] > data[left+1]:
                left += 1

            if data[left] < data[par_node]:
                data[left], data[par_node] = data[par_node], data[left]
                par_node = left
                left = 2 * par_node + 1
            else:
                break

if __name__ == "__main__":
    list2 = [4, 7, 0, 9, 1, 5, 3, 3, 2, 6]
    a1 = Solution1()
    b1 = a1.min_heap_sort(list2)
    print(b1)        # [0, 1, 2, 3, 3, 4, 5, 6, 7, 9]

# 列表res过程：
# [0]
# [0, 1]
# [0, 1, 2]
# [0, 1, 2, 3]
# [0, 1, 2, 3, 3]
# [0, 1, 2, 3, 3, 4]
# [0, 1, 2, 3, 3, 4, 5]
# [0, 1, 2, 3, 3, 4, 5, 6]
# [0, 1, 2, 3, 3, 4, 5, 6, 7]
# [0, 1, 2, 3, 3, 4, 5, 6, 7, 9]
