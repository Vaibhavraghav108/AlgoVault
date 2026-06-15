class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dict={}
        for i in s:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        for i in t:
            if i in dict:
                dict[i]-=1
            else:
                return False
        if not all(value==0 for value in dict.values()):
            return False
        return True
        
            