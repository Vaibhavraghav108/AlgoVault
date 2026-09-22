class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph={i:[] for i in range(1,n+1)}
        for u,v,t in times:
            graph[u].append((v,t))
        #its basically dijjistra algo
        dist=[float('inf')]*(n+1)
        dist[k]=0
        heap=[(0,k)]
        while heap:
            time,node=heapq.heappop(heap)
            if time>dist[node]:
                continue
            
            for neighbor,edge_time in graph[node]:
                new_time=time+edge_time

                if new_time<dist[neighbor]:
                    dist[neighbor]=new_time
                    heapq.heappush(heap,(new_time,neighbor))
        if float('inf') in dist[1:]:
            return -1
        return max(dist[1:])