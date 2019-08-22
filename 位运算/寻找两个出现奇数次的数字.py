# coding=UTF-8
# 给出N个数（保证N为偶数），其中有且只有两个不同的数字出现了奇数次。请你找出他们来
# 例如：输入[1,2,3,4,5,1,4,5]   输出[2,3]

"""
异或运算
&  与
两个位都为1时，结果才为1     （统计奇数）

|  或    
两个位都为0时，结果才为0       （统计偶数）

^  异或
两个位相同为0，相异为1      (常用统计不相同数）

~  取反
0变1，1变0

<< 左移
各二进位全部左移若干位，高位丢弃，低位补0

>> 右移
各二进位全部右移若干位，对无符号数，高位补0，有符号数，各编译器处理方法不一样，有的补符号位（算术右移），有的补0（逻辑右移）
"""

class Solution(object):
    def re(self, num):
        # 首先求出两个奇数次数字的异或结果
        result = num[0]
        for i in range(1,len(num)):
            result ^= i
        #　确定1的索引位数（从右往左看）
        index_1 = bin(result)[::-1].index('1')
        # 把原数组分为两个子数组
        a = [];b = []
        for i in range(len(num)):
            if bin(num[i])[::-1][index_1] == '0':
                a.append(num[i])
            elif bin(num[i])[::-1][index_1] == '1':
                b.append(num[i])
        print(a)
        print(b)
        # 各自异或，可以得到结果
        a1 = a[0];b1 = b[0]
        for i in range(1,len(a)):
            a1 ^= a[i]
        for i in range(1,len(b)):
            b1 ^= b[i] 
        
        return [a1, b1]

a = Solution()
b = a.re([1,2,3,4,5,1,4,5,6,7,2,6])
print(b)


for i  in range(100): 
    if i&1==1:
        print(i)