class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        seen=set()
        dict={}
        count=0
        for right in range(0,len(s)):
            if s[right] in dict:
                dict[s[right]]+=1
            else:
                dict[s[right]]=1
            lenght=(right-left)+1
            result=lenght-max(dict.values())
            while result>k:
                dict[s[left]]-=1
                left+=1
                lenght=(right-left)+1
                result=lenght-max(dict.values())
            count=max(count,lenght)
        return count       
        