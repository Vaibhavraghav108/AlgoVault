class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        queue=deque()
        fresh=0
        for r in range(row):
            for c in range(col):
                if grid[r][c]==2:
                    queue.append((r,c))
                elif grid[r][c]==1:
                    fresh+=1
        min=0
        while len(queue)!=0 and fresh>0:
            min+=1
            rotten=len(queue)
            for _ in range(rotten):
                i,j=queue.popleft()

                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    new_i,new_j=i+dx,j+dy

                    if new_i<0 or new_i==row or new_j<0 or new_j==col:
                        continue
                    elif grid[new_i][new_j]==0 or grid[new_i][new_j]==2:
                        continue
                    fresh-=1
                    grid[new_i][new_j]=2
                    queue.append((new_i,new_j))
        if fresh>0:
            return -1
        return min