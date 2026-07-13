class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dict={
                ")": "(",
                "]": "[",
                "}": "{"
        }
        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if not stack or stack.pop()!=dict[i]:
                    return False
        return len(stack)==0

