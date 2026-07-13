class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for i in range(0,len(s2)):
            if sorted(s1)==sorted(s2[i:i+len(s1)]):
                return True
        return False