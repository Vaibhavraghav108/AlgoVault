class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left=0
        right=0
        count=0
        dict={}
        while right<len(s):
            if s[right] in dict:
                dict[s[right]]+=1
            else:
                dict[s[right]]=1
            lenght=right-left+1
            if lenght-max(dict.values())>k:
                dict[s[left]]-=1
                left+=1
            count=max(count,right-left+1)
            right+=1
        return count
            