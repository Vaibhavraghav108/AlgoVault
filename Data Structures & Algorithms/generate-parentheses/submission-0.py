class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        sol=[]
        def backtrack(openp,closep):
            if openp==n and closep==n:
                result.append("".join(sol[:]))
                return
            if openp<n:
                sol.append('(')
                backtrack(openp+1,closep)
                sol.pop()
            if closep<openp:
                sol.append(')')
                backtrack(openp,closep+1)
                sol.pop()
        backtrack(0,0)
        return result
