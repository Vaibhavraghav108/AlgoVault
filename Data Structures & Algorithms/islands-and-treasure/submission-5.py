class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row=len(grid)
        col=len(grid[0])
        INF = 2147483647
        queue=deque()
        for rows in range(row):
            for cols in range(col):
                if grid[rows][cols]==0:
                    queue.append((rows,cols))
        while len(queue)!=0:
            i,j=queue.popleft()
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                new_dx,new_dy=i+dx,j+dy
                if new_dx<0 or new_dx>=row or new_dy<0 or new_dy>=col:
                    continue
                if grid[new_dx][new_dy]==-1 or grid[new_dx][new_dy]==0:
                    continue
                if grid[new_dx][new_dy]!=INF:
                    continue
                grid[new_dx][new_dy]=grid[i][j]+1
                queue.append((new_dx,new_dy))
                