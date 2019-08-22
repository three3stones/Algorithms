# 0 1 背包问题
# 有n个物品，它们有各自的体积和价值，现有给定容量的背包，如何让背包里装入的物品具有最大的价值总和？
# dp[i][j] 表示当前背包容量 j，前 i 个物品最佳组合对应的价值

"""
面对当前商品有两种可能性：
包的容量比该商品体积小，装不下，此时的价值与前i-1个的价值是一样的，即V(i,j)=V(i-1,j)；
还有足够的容量可以装该商品，但装了也不一定达到当前最优价值，所以在装与不装之间选择最优的一个，
即V(i,j)=max｛V(i-1,j)，V(i-1,j-w(i))+v(i)｝。
其中V(i-1,j)表示不装，V(i-1,j-w(i))+v(i) 表示装了第i个商品，背包容量减少w(i)，但价值增加了v(i)；
"""

class solution:
    def bag(self,weight,value,most_weight):
        """
        weight: list   value: list   most_weight: num
        """
        weight.insert(0,0)      # 增加0表示前0个物品的  
        value.insert(0,0)
        dp = [[0 for i in range(most_weight+1) ]for i in range(len(weight))]
        
        for i in range(1,len(weight)):      # 索引从1开始
            for j in range(1,most_weight+1):
                if j < weight[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]]+value[i])
        return dp[-1][-1],dp


if __name__ == "__main__":
    a = solution()
    b = a.bag([2,3,4,5],[3,4,5,6],8)
    print(b)
