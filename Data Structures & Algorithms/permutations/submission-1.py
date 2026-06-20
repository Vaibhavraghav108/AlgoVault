class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        sol=[]
        def backtrack(i):
            if len(sol)==len(nums):
                result.append(sol[:])
                return 
            for i in range(0,len(nums)):
                if nums[i] in sol:
                    continue
                sol.append(nums[i])
                backtrack(i)
                sol.pop()
        backtrack(0)
        return result