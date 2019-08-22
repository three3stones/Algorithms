# 爬楼梯
# 你需要攀爬一个有n个台阶的梯子
# 每一次你只能走1步或者两步，计算有多少中不同的登顶方式
# 注意:n必为正整数

# 输入： 3 
# 输出： 3 
# 解释： 有三种方法可以爬到楼顶。 
# 1. 1 步 + 1 步 + 1 步 
# 2. 1 步 + 2 步 
# 3. 2 步 + 1 步

"""
假设梯子有n层，那么如何爬到第n层呢，因为每次只能怕1或2步，那么爬到第n层的方法要么是从第n-1层一步上来的，要不就是从n-2层2步上来的
所以递推公式非常容易的就得出了：
                                    dp[n] = dp[n-1] + dp[n-2]
"""

def climbStairs(n):
    if n<=2:
        return n
    templist = [0,1,2]       # 记录每层楼梯有多少种登顶方式
    for i in range(3,n+1):
        templist.append(templist[-1]+templist[-2])
    return templist[-1]


if __name__ == '__main__':
    print(climbStairs(3))       # 3
    print(climbStairs(10))      # 89