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
        for i in range(0,len(t)):
            if t[i] not in dict:
                return False
            else:
                dict[t[i]]-=1
        if (all(i==0 for i in dict.values())):
            return True
        else:
            return False

        
            