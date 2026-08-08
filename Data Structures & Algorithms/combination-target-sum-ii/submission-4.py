class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sol=[]
        result=[]
        candidates.sort()
        def backtrack(start,target):
            if target==0:
                result.append(sol[:])
                return 
            if target<0:
                return 
            prev=None
            for i in range(start,len(candidates)):
                if candidates[i]==prev:
                    continue
                if candidates[i]>target:
                    break
                prev=candidates[i]
                sol.append(candidates[i])
                backtrack(i+1,target-candidates[i])
                sol.pop()
        backtrack(0,target)
        return result