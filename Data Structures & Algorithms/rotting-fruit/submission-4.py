class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        fresh=0
        queue=[]
        for rows in range(row):
            for cols in range(col):
                if grid[rows][cols]==2:
                    queue.append((rows,cols))
                elif grid[rows][cols]==1:
                    fresh+=1
        minutes=0
        while len(queue)!=0 and fresh>0:
            minutes+=1
            rotten=len(queue)
            for k in range(rotten):
                i,j=queue.pop(0)
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    new_i,new_j=i+dx,j+dy
                    if new_i<0 or new_i>=row or new_j<0 or new_j>=col:
                        continue
                    if grid[new_i][new_j]==0 or grid[new_i][new_j]==2:
                        continue
                    fresh-=1
                    grid[new_i][new_j]=2
                    queue.append((new_i,new_j))
        if fresh>0:
            return -1
        return minutes