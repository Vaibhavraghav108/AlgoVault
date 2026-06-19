class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        sol=[]
        def backtrack(i,target):
            if target==0:
                result.append(sol[:])
                return
            if i==len(nums) or target<0:
                return
            #skip
            backtrack(i+1,target)
            #dont skip
            sol.append(nums[i])
            backtrack(i,target-nums[i])
            sol.pop()
        backtrack(0,target)
        return result