class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]
        for i in nums:
            heapq.heappush(heap,-i)
        for i in range(0,k-1):
            heapq.heappop(heap)
        a=-heapq.heappop(heap)
        return a