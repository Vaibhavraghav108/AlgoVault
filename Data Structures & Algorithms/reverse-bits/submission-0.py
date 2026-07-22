class Solution:
    def reverseBits(self, n: int) -> int:
        result=bin(n)[2:].zfill(32)
        a = result[::-1]
        ans=int(a,2)

        return ans