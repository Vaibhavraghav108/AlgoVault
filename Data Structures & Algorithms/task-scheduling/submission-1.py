class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dict={}
        for i in range(0,len(tasks)):
            if tasks[i] in dict:
                dict[tasks[i]]+=1
            else:
                dict[tasks[i]]=1
        heap=[-i for i in dict.values()]
        heapq.heapify(heap) #[-3,-1,-1]
        freq_max=-heapq.heappop(heap) #3
        slots=(freq_max-1)*n
        while heap and slots>0:
            next_freq=-heapq.heappop(heap)#1
            slots-=min(freq_max-1,next_freq)
        slots=max(0,slots)

        return len(tasks)+slots
        