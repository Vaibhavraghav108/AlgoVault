class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        current_island = 0
        def dfs(r,c):
            nonlocal current_island
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]) or grid[r][c] != 1:
                return
            current_island += 1
            grid[r][c] = 0
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            return current_island
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    dfs(r,c)
                    result = max(result,current_island)
                    current_island = 0
        return result