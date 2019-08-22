# 和为S的连续正数序列
# 小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
# 但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
# 没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列?

"""
使用滑动窗口来求解这道题，核心思想就是设定一个大小不固定的窗口来圈住目标列表，如果列表中的数据满足条件就添加到答案中，否则就动态的移动该滑动窗口。

使用滑动窗口的方法来解决，
设定一个动态的窗口,p_low指向窗口头部，
p_high指向窗口尾部，窗口之间的值，为目标值。
如果目标值为tsum，那就是其中一个解。否则移动窗口。
"""
class Solution:
    def FindContinuousSequence(self, tsum):
        #错误判断处理，如果小于3的话 无解
        if tsum < 3:
            return []
        #设定初始的滑动窗口大小
        p_low = 1
        p_high = 2

        ans = []
        while p_low < p_high:
            #计算滑动窗口现在圈中的大小
            cur_sum = sum(range(p_low,p_high+1))
            if cur_sum == tsum:
                #找到一组解，并记录到ans数组中。
                ans.append(list(range(p_low,p_high+1)))
                #移动滑动窗口，并寻找下一组解。
                p_high = p_high + 1
            elif cur_sum < tsum:
                p_high = p_high + 1
            else :
                p_low = p_low + 1
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.FindContinuousSequence(100))
