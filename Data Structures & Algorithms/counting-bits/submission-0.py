class Solution:
    def countBits(self, n: int) -> List[int]:
        result=[]
        for i in range(0,n+1):
            a=bin(i)[2:]
            result.append(a.count("1"))
        return result