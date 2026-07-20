class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for i in stones:
            heapq.heappush(heap,-i)
        # heap=[-6,-4,-3,-2,-2]

        while len(heap)>1:
            y=-heapq.heappop(heap)
            x=-heapq.heappop(heap)
            if y==x:
                continue
            if y>x:
                z=y-x
                heapq.heappush(heap,-z)
        return -heap[0] if heap else 0
