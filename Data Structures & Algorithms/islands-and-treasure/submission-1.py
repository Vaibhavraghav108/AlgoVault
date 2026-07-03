class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row=len(grid)
        col=len(grid[0])
        queue=deque()
        INF = 2147483647
        for i in range(row):
            for j in range(col):
                if grid[i][j]==0:
                    queue.append((i,j))
        distance=0
        while len(queue)!=0:
            i,j=queue.popleft()
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                new_i,new_j=i+dx,j+dy

                if new_i<0 or new_i>=row or new_j<0 or new_j>=col:
                    continue
                if grid[new_i][new_j]!=INF:
                    continue
                grid[new_i][new_j]=grid[i][j]+1
                queue.append((new_i,new_j))
        