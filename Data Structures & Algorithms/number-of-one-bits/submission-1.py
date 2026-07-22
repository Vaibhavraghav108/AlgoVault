class Solution:
    def hammingWeight(self, n: int) -> int:
        '''
        n = 23
        binary = bin(n)
        print(binary)
        
        # 0b10111   to remove 0b -> binary = bin(n)[2:]
        '''
        count=0
        result=bin(n)[2:]
        for i in str(result):
            if i=='1':
                count+=1
        return count