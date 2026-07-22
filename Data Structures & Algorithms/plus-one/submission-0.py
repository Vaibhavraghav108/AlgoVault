class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits

            digits[i] = 0

        return [1] + digits

'''
dry run 989
digit[i] means digit[2]==9<9 no so digit[i]=0 
then digit[1]==8<9 yes digit[1]+=1 mean 8+1=9
then return
990 

'''