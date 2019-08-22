#  coding=UTF-8
#  判断一个数字是否是 N 的幂

"""
python中二进制函数 bin()　会在前面补上 "0b" ,返回一个字符串对象
如：bin(1) →　"0b1"  bin(4) →　"0b100"
因此，计数时要特别注意一下
"""

# 判断一个数字是否为２的幂
"""
如果一个数是２的幂，那么它的二进制数中只有一个1，其余的都为0
"""
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n > 0:
            from collections import Counter
            list_n = Counter(list(bin(n)))
            return list_n['1'] == 1
        else:
            return False

# 判断一个数字是否为4的幂
"""
如果一个数是4 幂，那么它的二进制数中奇数位是1且只有一个，其余的都为0
"""
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type n: int
        :rtype: bool
        """
        if num > 0:
            from collections import Counter
            list_n = Counter(list(bin(num)))
            if list_n['1'] == 1 and (list_n['0']+ list_n['b']) % 2 == 0:
                return True
            else:
                return False
        else:
            return False


# 判断一个数字是否为3的幂
"""
3的幂没有什么规律，因此可以使用通用的解法　——　取对数
"""
class Solution(object):
    def isPowerOfThree(self, num):
        """
        :type n: int
        :rtype: bool
        """
        if num > 0:
            import math
            result = math.log(num,3)
            return result == int(result)
        else:
            return False
