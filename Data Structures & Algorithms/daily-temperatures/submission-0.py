class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        lst=[]
        result=[0]*len(temperatures)
        for right in range(0,len(temperatures)):
            while lst and temperatures[right]>temperatures[lst[-1]]:
                left=lst.pop()
                result[left]=(right-left)
            lst.append(right)
        return result