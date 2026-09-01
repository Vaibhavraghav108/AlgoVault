class Solution:
    def checkValidString(self, s: str) -> bool:
        open=[]
        star=[]
        for i in range(len(s)):
            if s[i]=='(':
                open.append(i)
            elif s[i]=='*':
                star.append(i)
            else:  # ')'
                if open:
                    open.pop()
                elif star:
                    star.pop()
                else:
                    return False
        # Match remaining '(' with '*'
        while open:
            if not star:
                return False
            if open[-1] < star[-1]:
                open.pop()
                star.pop()
            else:
                return False
        return True