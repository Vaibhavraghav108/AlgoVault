class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:

        candidates.sort()        
        result = []
        sol = []
        def backtrack(start, target):
            if target == 0:
                result.append(sol[:])
                return
            if target < 0:
                return
            for i in range(start, len(candidates)):
                # If it's a duplicate at the SAME level of decisions, skip it!
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                    
                # dont skip
                sol.append(candidates[i])
                backtrack(i + 1, target - candidates[i])
                sol.pop()
        backtrack(0, target)
        return result