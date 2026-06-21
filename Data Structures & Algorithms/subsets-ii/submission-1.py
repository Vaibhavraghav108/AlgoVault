class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        sol=[]
        def backtrack(i):
            if i==len(nums):
                if sorted(sol) not in result:
                    result.append(sol[:])
                return
            #dont skip
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

            #skip
            backtrack(i+1)
        backtrack(0)
        return result