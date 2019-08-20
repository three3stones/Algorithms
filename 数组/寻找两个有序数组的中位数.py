# coding=UTF-8
# 4. 寻找两个有序数组的中位数
# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        half = len(nums1) // 2
        return (nums1[half] + nums1[~half]) / 2

a = Solution()
b = a.findMedianSortedArrays([1,7,9,16],[12,25,36,78])
print(b)

c = [1,2,3,4,5,6,7,8]
print(c[3])
print(c[~3])