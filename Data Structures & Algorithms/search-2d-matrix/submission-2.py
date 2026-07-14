class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        result=[]
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                result.append(matrix[i][j])
        left=0
        right=len(result)-1
        while left<=right:
            mid=(left+right)//2
            if result[mid]==target:
                return True
            elif result[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return False