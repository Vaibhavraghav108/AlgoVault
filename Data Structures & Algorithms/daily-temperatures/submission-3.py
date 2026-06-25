class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        for i in range(0,len(temperatures)):
            left=i
            right=i+1
            while right<len(temperatures):
                if temperatures[right]>temperatures[left]:
                    result[left]=right-left
                    break
                else:
                    right+=1
        return result