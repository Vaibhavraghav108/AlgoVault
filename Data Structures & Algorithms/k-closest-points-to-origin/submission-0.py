class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        ans=[]
        for i in range(len(points)):
            distance=math.sqrt((0-int(points[i][0]))**2+(0-int(points[i][1]))**2)
            heapq.heappush(heap,(distance,points[i]))
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans