class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:


        if len(edges)!=n-1:
            return False
        adj_list=[[] for i in range(n)]
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        vis=[0 for _ in range(n)]

        '''
        why are we not returning anything
        The dfs() function here is not returning any value because its
        purpose is not to compute something. Its purpose is to modify the vis list.
        '''
        def dfs(node):
            vis[node]=1
            for nei in adj_list[node]:
                if vis[nei]==0:
                    dfs(nei)
        dfs(0)

        return all(vis)