class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph=defaultdict(list)

        def dfs(node,target,visited):
            visited[node]=True
            if node==target:
                return True
            for nei in graph[node]:
                if visited[nei]==False:
                    if dfs(nei,target,visited):
                        return True
            return False
        
        for u,v in edges:
            if u in graph and v in graph:
                visited=[False]*(len(edges)+1) # total 4 edges so we need 5 size visited array
                if dfs(u,v,visited): # if this is true then we have found a cycle
                    return [u,v]
            graph[u].append(v)
            graph[v].append(u)
        return []