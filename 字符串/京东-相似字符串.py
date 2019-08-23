# 京东-相似字符串
# 输入两个字符串S, T，假如S的子串与T串的格式相同，则认为相似。
# 如：S:ababcb, T:xyx,  则S中aba,bab, bcb与T串相似，输出3.

"""
使用滑动窗口，一一判断子串和T串是否格式相同
考虑以下情况：
    第一轮判断：
    'abc' 'xyx'  两者set后，长度不一致，直接排除
    'abb' 'yyx'  两者set后，长度一致，进入下一轮
    第二轮判断：
    'abb' 'yyx'  对应组合[(a,y),(b,y),(b,x)] 取set后，长度和之前不一致，要排除
    'abb' 'yxx'  对应组合[(a,y),(b,x),(b,x)] 取set后，长度和之前一致，故为相似字符串
"""

class solution:
    def res(self,s,t):
        if s is None or t is None:
            return 0
        ls, lt = len(s), len(t)
        diff = ls-lt+1
        count = 0
        for i in range(diff):
            temp = []      # 每次i更新，temp都会置空
            new = s[i:i+lt]
            if len(set(new)) == len(set(t)):    # 第一轮
                temp = list(zip(new,t))
                if len(set(temp)) == len(set(t)):   # 第二轮
                    count += 1
        return count

if __name__ == "__main__":
    a = solution()
    b = a.res('ababcb','xyx')
    print(b)


