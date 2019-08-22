# coding=UTF-8
# 415. 字符串相加       类似于链表相加
# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
# 注意：
# num1 和num2 的长度都小于 5100.
# num1 和num2 都只包含数字 0-9.
# num1 和num2 都不包含任何前导零。
# 你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。

'''
我的思路：
1、先将字符串都倒序，因为从个位数开始加起
2、用0在末尾填充，保证两个字符串长度一致
3、增加一个变量add，表示进位多少；res用来拼接结果
4、%取余数得到当前位的数字，//得到进位数字。
5、不能忘记最后还有一个进位要加上，如果进位是0，则不用加上
6、将结果字符串res翻转过来
'''


class Solution:
    def addStrings(self, num1, num2):
        num1_re = num1[::-1]
        num2_re = num2[::-1]
        l_m = max(len(num1), len(num2))
        num1_re += "0" * (l_m-len(num1))
        num2_re += "0" * (l_m-len(num2))
        
        add = 0 ; res = ""
        for i in range(l_m):
            su = int(num1_re[i]) + int(num2_re[i]) + add
            res += str(su % 10)
            add = su // 10
        # 考虑到最后一位是否需要进位
        if add != 0:
            res += str(add)
        res = res[::-1]
        return res

a = Solution()
b = a.addStrings("12","123")
print(b)
