class Solution:
    def isPalindrome(self, s: str) -> bool:
        z="".join(i.lower() for i in s if i.isalnum())
        left=0
        right=len(z)-1
        while (left<right):
            if z[left]!=z[right]:
                return False
            left+=1
            right-=1
        return True
        