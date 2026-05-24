class Solution:
    def isPalindrome(self, s: str) -> bool:
        x="".join(i.lower() for i in s if i.isalnum())
        left=0
        right=len(x)-1
        while (left<right):
            if x[left]!=x[right]:
                return False
            left+=1
            right-=1
        return True
        