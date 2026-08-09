class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        sol=[]
        def backtrack(openb,closeb):
            if openb==n and closeb==n:
                result.append("".join(sol[:]))
                return 
            if openb<n:
                sol.append('(')
                backtrack(openb+1,closeb)
                sol.pop()
            if closeb<openb:
                sol.append(')')
                backtrack(openb,closeb+1)
                sol.pop()
        backtrack(0,0)
        return result