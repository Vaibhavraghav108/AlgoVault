class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=set()
        col=set()
        box=set()
        
        for i in range(0,len(board)):
            for j in range(0,len(board)):
                if board[i][j]==".":
                    continue
                if (i,board[i][j]) in row:
                    return False
                row.add((i,board[i][j]))
                if (j,board[i][j]) in col:
                    return False
                col.add((j,board[i][j]))

                boxes=((i//3),(j//3))
                if (boxes,board[i][j]) in box:
                    return False
                box.add((boxes,board[i][j]))
        return True
    