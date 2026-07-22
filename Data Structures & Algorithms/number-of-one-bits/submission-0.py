class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        binary = ""
        while n > 0:
            remainder = n % 2
            binary += str(remainder)
            n = n // 2

        binary = binary[::-1]

        for i in binary:
            if i=='1':
                count+=1
        return count