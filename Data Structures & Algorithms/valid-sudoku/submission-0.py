class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n=len(board)
        box_size=math.sqrt(n)
        col=[[] for _ in range(n)]
        rows=[[] for _ in range(n)]
        box=[[] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if board[i][j]==".":
                    continue
                if board[i][j] in col[i]:
                    return False
                col[i].append(board[i][j]) 
                if board[i][j] in rows[j]:
                    return False
                rows[j].append(board[i][j])
                box_number=int(self.getboxindex(i,j,box_size))
                if board[i][j] in box[box_number]:
                    return False
                box[box_number].append(board[i][j])
        return True
    def getboxindex(self,i,j,n):
        row_band=j//n
        col_band=i//n
        return row_band*n+col_band


        