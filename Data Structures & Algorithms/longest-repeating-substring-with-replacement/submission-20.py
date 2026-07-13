class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict={}
        left=0
        result=0
        for right in range(0,len(s)):
            if s[right] in dict:
                dict[s[right]]+=1
            else:
                dict[s[right]]=1
            while (right-left+1)-max(dict.values())>k:
                dict[s[left]]-=1
                left+=1
            result=max(result,right-left+1)
        return result