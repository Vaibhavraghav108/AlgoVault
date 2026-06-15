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
        def check(window,need):
            for i in need:
                if i not in window or window[i]<need[i]:
                    return False
            return True
        
        window={}
        left=0
        count=0
        streak=0
        for right in range(0,len(s)):
            if s[right] in window:
                window[s[right]]+=1
            else:
                window[s[right]]=1
            while check(window,need):

                if count==0 or right-left+1<count:
                    count=right-left+1
                    streak=left
                window[s[left]]-=1
                left+=1
        return s[streak:streak+count] if count > 0 else ""