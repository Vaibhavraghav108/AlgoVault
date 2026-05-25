class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0
        dict = {}
        count = 0

        for right in range(len(s)):
            if s[right] in dict:
                dict[s[right]] += 1
            else:
                dict[s[right]] = 1

            while (right - left + 1) - max(dict.values()) > k:
                dict[s[left]] -= 1
                left += 1

            count = max(count, right - left + 1)

        return count   
            