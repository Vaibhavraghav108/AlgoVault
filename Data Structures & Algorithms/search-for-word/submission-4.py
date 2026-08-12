class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row=len(board)
        col=len(board[0])

        def backtrack(r,c,i):
            if i==len(word):
                return True

            if r<0 or c<0 or r>=row or c>=col:
                return False
            
            if board[r][c]!=word[i]:
                return False
            
            temp=board[r][c]
            board[r][c]='#'

            found= (backtrack(r+1,c,i+1) or 
                    backtrack(r-1,c,i+1) or
                    backtrack(r,c+1,i+1) or
                    backtrack(r,c-1,i+1))
            board[r][c]=temp

            return found

        
        for rows in range(row):
            for cols in range(col):
                if board[rows][cols]==word[0]:
                    if backtrack(rows,cols,0):
                        return True
        return False