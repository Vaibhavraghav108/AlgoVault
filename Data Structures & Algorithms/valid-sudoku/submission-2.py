class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=set()
        col=set()
        boxes=set()
        for i in range(0,9):
            for j in range(0,9):
                num=board[i][j]
                if num==".":
                    continue
                if (i,num) in row:
                    return False
                row.add((i,num))
                ######################
                if (j,num) in col:
                    return False
                col.add((j,num))
                ######################
                box= (i//3,j//3)
                ######################
                if (box,num) in boxes:
                    return False
                boxes.add((box,num))
        return True
    