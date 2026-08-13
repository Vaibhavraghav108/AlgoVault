class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits :
            return []

        dic={
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        result=[]
        sol=[]
        def backtrack(i):
            if i==len(digits):
                result.append("".join(sol))
                return 
            words=dic[digits[i]]
            for j in words:
                sol.append(j)
                backtrack(i+1)
                sol.pop()
        backtrack(0)
        return result