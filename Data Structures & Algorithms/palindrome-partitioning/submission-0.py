class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result=[]
        sol=[]

        def backtrack(start):
            if start==len(s):
                result.append(sol[:])
                return 
            
            for end in range(start,len(s)):
                x=s[start:end+1]
                if x==x[::-1]:
                    sol.append(x)
                    backtrack(end+1)
                    sol.pop()
        backtrack(0)
        return result