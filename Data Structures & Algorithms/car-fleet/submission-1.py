class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet=1
        lst=[]
        dict={} #[4,1,0,7]
        for i in range(0,len(position)):
            time=(target-position[i])/speed[i]
            dict[position[i]]=time
        for i in sorted(dict):
            lst.append(dict[i])
        while len(lst)>1:
            a=lst.pop()
            b=lst.pop()
            if b<=a:
                fleet=fleet
                lst.append(a)
            else:
                fleet+=1
                lst.append(b)
        return fleet