class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        sol=[]
        total=n*2
        '''
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
        '''
        def backtrack(i,count):
            if count<0:
                return
            if count>n:
                return
            if i==total:
                if count==0:
                    result.append("".join(sol[:]))
                return
            # take (
            sol.append('(')
            backtrack(i+1,count+1)
            sol.pop()

            # take )
            if count>0:
                sol.append(')')
                backtrack(i+1,count-1)
                sol.pop()
        backtrack(0,0)
        return result
