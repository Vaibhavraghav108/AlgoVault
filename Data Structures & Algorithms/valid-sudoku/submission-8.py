class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=set()
        col=set()
        box=set()
        for i in range(0,9):
            for j in range(0,9):
                nums=board[i][j]
                boxes=(i//3,j//3)
                if nums=='.':
                    continue
                if (i,nums) in row or (j,nums) in col or (boxes,nums) in box:
                    return False
                row.add((i,nums))
                col.add((j,nums))
                box.add((boxes,nums))
        return True

                     