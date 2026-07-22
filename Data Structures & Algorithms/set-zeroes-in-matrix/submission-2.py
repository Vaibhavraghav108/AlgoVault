class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        row=set()
        col=set()
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if matrix[i][j]==0:
                    row.add(i)
                    col.add(j)
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if i in row or j in col:
                    matrix[i][j]=0
        