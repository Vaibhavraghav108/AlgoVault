class Solution:
    def reverse(self, x: int) -> int:
        a=str(x)[::-1]
        v=0
        if a[-1]=='-':
            v=-int(a[:-1])
        else:
            v=int(a)
        if not (-2**31<=v<=2**31-1):
            return 0
        return v