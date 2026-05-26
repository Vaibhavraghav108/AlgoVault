class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s1)
        s1=sorted(s1)
        for i in range(0,len(s2)-n+1): # normally len(s2) can also work 
            if sorted(s2[i:i+n])==s1:
                return True
        return False