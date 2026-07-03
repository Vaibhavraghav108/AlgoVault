class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row=len(grid)
        col=len(grid[0])
        def dfs(r,c,dist):
            if r<0 or r>=row or c<0 or c>=col:
                return 
            if grid[r][c]==-1:
                return 
            if grid[r][c]!=0 and dist>=grid[r][c]:
                return 
            
            if grid[r][c]!=0:
                grid[r][c]=dist
        
            dfs(r+1,c,dist+1)
            dfs(r-1,c,dist+1)
            dfs(r,c+1,dist+1)
            dfs(r,c-1,dist+1)
        
        for r in range(row):
            for c in range(col):
                if grid[r][c]==0:
                    dfs(r,c,0)
        
