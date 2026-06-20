class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        sol=[]
        seen=set()
        def backtrack(i):
            if len(sol)==len(nums):
                result.append(sol[:])
                return 
            for i in range(0,len(nums)):
                if nums[i] in seen:
                    continue
                seen.add(nums[i])
                sol.append(nums[i])
                backtrack(i)
                sol.pop()
                seen.remove(nums[i])
        backtrack(0)
        return result