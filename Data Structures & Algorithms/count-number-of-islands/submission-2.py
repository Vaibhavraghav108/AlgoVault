class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row=len(grid)
        col=len(grid[0])
        count=0
        def dfs(r,c):
            if r<0 or r>=row or c<0 or c>=col:
                return
            if grid[r][c]=='0' or grid[r][c]=='#':
                return 
            grid[r][c]='#'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        for rows in range(row):
            for cols in range(col):
                if grid[rows][cols]=='1':
                    count+=1
                    dfs(rows,cols)
        return count