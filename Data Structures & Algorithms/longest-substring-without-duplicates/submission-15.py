class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        left=0
        streak=0
        for right in range(0,len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            streak=max(streak,len(seen))
        return streak