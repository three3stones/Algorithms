# 28.实现strStr()
# 给定一个 haystack 字符串和一个 needle 字符串
# 在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回 -1。


class Solution:
    def strStr(self, haystack, needle):
        if needle  not in haystack:
            return -1
        return haystack.find(needle)

# 切片法
    def strStr(self, haystack, needle):
        l = len(needle)
        for i in range(len(haystack)-l+1):
            if haystack[i:i+l] == needle:
                return i
        return -1


q = "a"
w = "a"

a = Solution()
b = a.strStr(q,w)
print(b)