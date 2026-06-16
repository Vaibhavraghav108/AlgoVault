class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for i in stones:
            heapq.heappush(heap,-i)
        while len(heap)>1:
            y=-heapq.heappop(heap)
            x=-heapq.heappop(heap)
            if y==x:
                if not heap:
                    return 0
                else:
                    pass
            if x<y:
                y=y-x
                heapq.heappush(heap,-y)
        return -heap[0]