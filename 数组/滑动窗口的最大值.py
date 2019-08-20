# coding=UTF-8
# 滑动窗口的最大值
# 给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口 k 内的数字。
# 滑动窗口每次只向右移动一位。  结果返回滑动窗口最大值。
# 输入：　[1,3,-1,-3,5,3,6,7] ,　k = 3
# 输出：  [3,3,5,5,6,7] 

"""
每次把window数组找出来然后暴力求最大值。
但是每一次循环不需要重新算整个temp，而是把队头pop，然后把新的元素压入队尾
"""
class solution:
    def windowMax(self, nums, k):
        l = len(nums)
        res = list()       # 存储最终结果   
        temp = nums[0:2]
        for i in range(2,l):        # 结果中包含 l-k+1 项元素
            temp.append(nums[i])
            res.append(max(temp))
            temp.pop(0)
        return res

if __name__ == "__main__":
    a = solution()
    b = a.windowMax([1,3,-1,-3,5,3,6,7],3)
    print(b)