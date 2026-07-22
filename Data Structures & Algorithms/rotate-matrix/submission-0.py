class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        result=[[] for i in range(len(matrix))]
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                result[i].append(matrix[j][i])
        for row in result:
            row.reverse()
        
        matrix[:]=result

