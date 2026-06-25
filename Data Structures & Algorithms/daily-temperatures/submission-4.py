class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        stack=[]
        for right in range(0,len(temperatures)):
            while stack and temperatures[right]>temperatures[stack[-1]]:
                left=stack.pop()
                result[left]=right-left
            stack.append(right)
        return result