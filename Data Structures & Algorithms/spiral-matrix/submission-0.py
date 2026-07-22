class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        visited = [[0] * cols for _ in range(rows)]
        directions = [(0,1), (1,0), (0,-1), (-1,0)]   # Right, Down, Left, Up
        d = 0

        r = 0
        c = 0

        result = []

        for _ in range(rows * cols):

            result.append(matrix[r][c])
            visited[r][c] = 1

            nr = r + directions[d][0]
            nc = c + directions[d][1]

            if (nr < 0 or nr >= rows or
                nc < 0 or nc >= cols or
                visited[nr][nc]):

                d = (d + 1) % 4
                
                nr = r + directions[d][0]
                nc = c + directions[d][1]
            r = nr
            c = nc
        return result