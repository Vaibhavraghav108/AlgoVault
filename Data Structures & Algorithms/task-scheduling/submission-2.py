class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dict={}
        for i in tasks:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        heap=[-i for i in dict.values()]
        heapq.heapify(heap)
        time=0
        queue=[] 
        while heap or queue:
            time+=1
            if heap:
                cnt=heapq.heappop(heap)+1
                if cnt<0:
                    queue.append((cnt, n + time))
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.pop(0)[0])
        return time
        