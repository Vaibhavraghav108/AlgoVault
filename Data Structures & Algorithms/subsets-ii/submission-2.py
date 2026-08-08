class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result=set()
        sol=[]
        def backtrack(i):
            if i==len(nums):
                result.add(tuple(sorted(sol)))
                return 
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

            backtrack(i+1)
        backtrack(0)
        return [list(i) for i in result]