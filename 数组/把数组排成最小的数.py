# 把数组排成最小的数
# 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
# 例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。

import itertools
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if len(numbers) == 0:       # 没有这个，不会 ac100%
            return ""
        temp = list(map(lambda x:str(x),numbers))       # 把列表内的数字转成字符串格式
        res = []
        for i in itertools.permutations(temp):      # 全排列
            res.append(int(''.join(i)))
        return min(res)

a = Solution()
b = a.PrintMinNumber([3,32,321])
print(b)