class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict={}
        if len(s)!=len(t):
            return False
        for i in range(0,len(s)):
            if s[i] in dict:
                dict[s[i]]+=1
            else:
                dict[s[i]]=1
        for j in range(0,len(t)):
            if t[j] in dict:
                dict[t[j]]-=1
            else:
                return False
        for i in dict.values():
            if i!=0:
                return False
        return True
             