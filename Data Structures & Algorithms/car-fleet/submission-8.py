class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dict={}
        fleet=1
        for i in range(0,len(position)):
            time=(target-position[i])/speed[i]
            dict[position[i]]=time
        stack=[]
        for i in sorted(dict):
            stack.append(dict[i])

        while len(stack)>1:
            a=stack.pop()
            b=stack.pop()
            if b<=a:
                fleet=fleet
                stack.append(a)
            else:
                fleet+=1
                stack.append(b)
        return fleet