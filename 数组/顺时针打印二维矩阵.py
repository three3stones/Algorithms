# 剑指offer面试题：输入一个矩阵,按照从外向里以顺时针的顺序依次打印出每一个数字 
class Solution:
    # matrix类型为二维列表，需要返回列表 
    def printMatrix(self, matrix):
        if matrix==[[]]:
            return
        row=len(matrix)
        column=len(matrix[0])
        left=0
        right=column-1
        top=0
        boom=row-1
        res=[]
        while right>left and top<boom:
            #从左到右
            for i in range(left,right+1):
                res.append(matrix[top][i])
            #从上到下
            for i in range(top+1,boom+1):
                res.append(matrix[i][right])
            #从右到左
            for i in range(right-1,left-1,-1):
                res.append(matrix[boom][i])
            #从下到上
            for i in range(boom-1,top,-1):
                res.append(matrix[i][left])
            left+=1
            right-=1
            top+=1
            boom-=1
        
        #剩下一行
        if boom==top and left<right:
            for i in range(left,right+1):
                res.append(matrix[boom][i])
        #剩下一列
        if left==right and boom>top:
            for i in range(top,boom+1):
                res.append(matrix[i][left])
        #剩下一个
        if boom==top and left==right:
            res.append(matrix[left][top])
        return res
