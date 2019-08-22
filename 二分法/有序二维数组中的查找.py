# coding=UTF-8
# 二维数组中的查找
# 题目描述:
# 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

"""
从左上角开始入手之所以不可行的原因，是因为以左上角为基准遍历时，满足条件的数字可能分布在两侧，所以并不能很好的缩小搜索范围。
以左下角或右上角为锚点开始查找，满足条件的数字值只可能分布在一侧，可以缩小搜索范围。
从某种角度看，这种解法类似于“二分法”，只不过不是严格意义上均匀的二分。
"""

class Solution(object):
    def find(self, array, target):
        xend = len(array)-1
        yend = len(array[0])-1
        x = 0           # 初始化行值
        while x <= xend and yend >= 0:      # 从右上角开始搜索
            if array[x][yend] == target:
                # print(x,yend) 　可输出目标值的位置索引
                return True
            elif array[x][yend] > target:
                yend -= 1
            else:
                x += 1
        return False

array1 = [[1,2,8,9],
          [2,4,9,12],
          [4,7,10,13],
          [6,8,11,15]]
a = Solution()
b = a.find(array1, target = 7)
print(b)

# 代码搜索路径　9 → 8 → 2 → 4 → 7