class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''lst=[]
        result=[0]*len(temperatures)
        for right in range(0,len(temperatures)):
            while lst and temperatures[right]>temperatures[lst[-1]]:
                left=lst.pop()
                result[left]=(right-left)
            lst.append(right)
        return result
        '''
        n = len(temperatures)
        ans = [0] * n

        for left in range(n):
            right = left + 1

            while right < n:
                if temperatures[right] > temperatures[left]:
                    ans[left] = right - left
                    break
                right += 1

        return ans