class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        cols=len(board[0])
        def backtrack(r,c,i):
            if i==len(word):
                return True
            
            if r<0 or c<0 or r>=rows or c>=cols:
                return False
            
            if board[r][c]!=word[i]:
                return False
            temp=board[r][c]
            board[r][c]='#'
            direction=(
                backtrack(r+1,c,i+1) or
                backtrack(r-1,c,i+1) or
                backtrack(r,c+1,i+1) or
                backtrack(r,c-1,i+1) 
            )

            board[r][c]=temp


            return direction
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col]==word[0]:
                    if backtrack(row,col,0):
                        return True
        return False
