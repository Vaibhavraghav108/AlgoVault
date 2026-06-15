class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        need={}
        for i in t:
            if i in need:
                need[i]+=1
            else:
                need[i]=1
        window={}
        count=0
        left=0
        result=""
        for right in range(0,len(s)):
            if s[right] in window:
                window[s[right]]+=1
            else:
                window[s[right]]=1
            while all(window.get(i,0)>=need[i] for i in need):
                if count==0 or right-left+1<count:
                    count=right-left+1
                    result=s[left:right+1]
                window[s[left]]-=1
                left+=1
        return result