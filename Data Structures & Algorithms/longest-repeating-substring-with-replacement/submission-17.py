class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict={}
        count=0
        left=0
        for right in range(0,len(s)):
            if s[right] in dict:
                dict[s[right]]+=1
            else:
                dict[s[right]]=1
            while (right-left)-max(dict.values())>=k:
                dict[s[left]]-=1 ## 5. If imposters exceed our cheat budget (k), we went broke! 
            #    Evict the leftmost letter and slide the window forward.
                left+=1
            count=max(count,right-left+1)
        return count
