# TOP K 问题  ------  堆排序
"""
复杂度：O(N*logK)
思路：
1. 取列表前Ｋ个元素建立一个小顶堆。堆顶就是目前第Ｋ大的数。
2. 依次向后遍历原列表，如果小于堆顶，则忽略此元素；如果大于堆顶，则将堆顶替换为该元素，并对堆进行一次调整。
3. 遍历列表所有元素后，倒序弹出堆顶。
"""

# 小顶堆
def min_heap_adjust(data,mid,high):
    par_node = mid
    left = par_node * 2 + 1
    
    while left <= high:
        if left != high and data[left] > data[left+1]:
            left += 1
        
        if data[left] < data[par_node]:
            data[left],data[par_node] = data[par_node],data[left]
            par_node = left
            left = left * 2 + 1
        else:
            break

def top_k(list1,k):
    heap = list1[:k]
    # 利用列表前Ｋ个元素建立小顶堆
    mid = k//2-1
    while mid >= 0:
        min_heap_adjust(heap,mid,k-1)
        mid -= 1

    # 依次向后遍历原列表，比较堆顶和原列表元素
    for i in range(k, len(list1)):
        if list1[i] > heap[0]:
            heap[0] = list1[i]
            min_heap_adjust(heap, 0, k - 1)

    # 挨个输出 --- 将小顶堆的堆顶元素和最后Ｋ位置的元素交换，然后对前 K-1 的元素建立最小堆
    for i in range(k - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        min_heap_adjust(heap, 0, i - 1)
    return heap

if __name__ == "__main__":
    li = [0, 8, 6, 2, 4, 9, 1, 4, 6]
    print(top_k(li, 3))