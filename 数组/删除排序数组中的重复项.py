# coding=UTF-8
# 26. 删除排序数组中的重复项
# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

"""
设立2个指针i，j。跑得快的指针j会在遇到不是重复的元素的时候停下来，此时i+1进行赋值。如此遍历即可。
"""

class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        j = 0
        while j < len(nums)-1:
            if nums[j] == nums[j+1]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j+1]
                j += 1
        return len(set(nums))

a = Solution()
b = a.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(b)
