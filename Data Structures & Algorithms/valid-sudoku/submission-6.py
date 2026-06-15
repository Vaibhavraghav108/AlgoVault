class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=set()
        col=set()
        box=set()
        for i in range(0,9):
            for j in range(0,9):
                num=board[i][j]
                if num==".":
                    continue
                if (i,num) in row or (j,num) in col or (i//3,j//3,num) in box:
                    return False
                row.add((i,num))
                col.add((j,num))
                box.add((i//3,j//3,num))
        return True
