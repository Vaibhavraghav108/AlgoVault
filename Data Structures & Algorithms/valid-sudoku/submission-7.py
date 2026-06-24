class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
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
    '''
        row=set()
        col=set()
        box=set()
        for i in range(0,9):
            for j in range(0,9):
                nums=board[i][j]
                if nums=='.':
                    continue
                if (i,nums) in row:
                    return False
                row.add((i,nums))

                if (j,nums) in col:
                    return False
                col.add((j,nums))

                boxes=(i//3,j//3)
                if (boxes,nums) in box:
                    return False
                box.add((boxes,nums))
        return True