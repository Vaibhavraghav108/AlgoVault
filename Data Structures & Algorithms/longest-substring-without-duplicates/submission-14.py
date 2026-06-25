class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        left=0
        right=0
        count=1
        seen=set()
        if not s:
            return 0
        while right<len(s):
            if s[right] not in seen:
                seen.add(s[right])
                right+=1
                count=max(count,right-left)
            else:
                seen.remove(s[left])
                left+=1
        return count
''' 
        seen=set()
        count=0
        left=0
        for right in range(0,len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            count=max(count,len(seen))
        return count