class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lst=[]
        for i in matrix:
            for j in i:
                lst.append(j) # just make a single list [1,2,4,8,10,11,12,13,14,20,30,40]
        
        left=0
        right=len(lst)-1
        while(left<=right):
            mid=(left+right)//2
            if lst[mid]==target:
                return True
            elif lst[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return False