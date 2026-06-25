class Solution:
    def isValid(self, s: str) -> bool:
        dict={
            '(':')',
            '{':'}',
            '[':']'
        }
        stack=[]
        for i in range(0,len(s)):
            if s[i] in '([{':
                stack.append(s[i])
            else:
                if not stack:
                    return False
                a=stack.pop()
                if dict[a]!=s[i]:
                    return False
        return not stack