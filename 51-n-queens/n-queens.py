class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board =[['.' for i in range(n)] for i in range(n)]
        rowSet = set()
        upperDiag = set()
        lowerDiag = set()

        def validBoard(row, col):
            if row in rowSet:
                return False

            if row + col in upperDiag:
                return False
            
            if row - col in lowerDiag:
                return False
            
            return True
        ans = []
        def backtrack(col):
            nonlocal ans
            if col == n:
                newBoard = []
                for row in board:
                    newBoard.append("".join(row))
                ans.append(newBoard)
                return
            for row in range(n):
                if validBoard(row, col):
                    board[row][col] = 'Q'
                    rowSet.add(row)
                    upperDiag.add(row + col)
                    lowerDiag.add(row - col)

                    backtrack(col + 1)

                    board[row][col] = '.'
                    rowSet.remove(row)
                    upperDiag.remove(row + col)
                    lowerDiag.remove(row - col)
        backtrack(0)
        return ans