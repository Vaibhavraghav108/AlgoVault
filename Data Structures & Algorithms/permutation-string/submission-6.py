class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s1)
        for i in range(0,len(s2)):
            if sorted(s1)==sorted(s2[i:n+i]):
                return True
        return False