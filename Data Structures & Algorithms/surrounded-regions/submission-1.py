class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row=len(board)
        col=len(board[0])

        def dfs(r,c):
            if r<0 or r>=row or c<0 or c>=col:
                return 
            if board[r][c]!='O':
                return 
            board[r][c]='T' # for visited
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        #top row
        for c in range(col):
            if board[0][c]=='O':
                dfs(0,c)
        #bottom row
        for c in range(col):
            if board[row-1][c]=='O':
                dfs(row-1,c)
        #left column
        for r in range(row):
            if board[r][0]=='O':
                dfs(r,0)
        #right column
        for r in range(row):
            if board[r][col-1]=='O':
                dfs(r,col-1)
        
        # traverse the board and change 'O' to 'X' and 'T' back to 'O'
        for r in range(row):
            for c in range(col):
                if board[r][c]=='O':
                    board[r][c]='X'
                elif board[r][c]=='T':
                    board[r][c]='O'
