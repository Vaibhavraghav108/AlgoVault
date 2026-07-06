class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list=[[] for _ in range(n)]
        vis=[0]*n
        count=0

        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        def dfs(node):
            vis[node]=1
            for nei in adj_list[node]:
                if vis[nei]==0:
                    dfs(nei)

        for i in range(n):
            if vis[i]==0:
                count+=1
                dfs(i)

        return count