class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dict={}
        count=1
        for i in range(0,len(position)):
            time=(target-position[i])/speed[i]
            dict[position[i]]=time
        stack=[]
        for i in sorted(dict,reverse=True):
            if not stack or dict[i]>stack[-1]:
                stack.append(dict[i])
        return len(stack)