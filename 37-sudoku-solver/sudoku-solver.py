class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rowHash = defaultdict(set)
        colHash = defaultdict(set)
        square = defaultdict(set)
        emp = []

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    rowHash[i].add(board[i][j])
                    colHash[j].add(board[i][j])
                    square[(i // 3, j // 3)].add(board[i][j])

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    emp.append((i, j))


        def isSafe(row, col, ch):
            if ch in rowHash[row]:
                return False
            
            if ch in colHash[col]:
                return False

            newRow = row // 3
            newCol = col // 3
                
            if ch in square[(newRow, newCol)]:
                return False
            
            return True

        def solve(ind):
            if ind == len(emp):
                return True
            i, j = emp[ind]
            for k in range(1,10):
                if isSafe(i, j, str(k)):
                    board[i][j] = str(k)
                    newRow = i // 3
                    newCol = j // 3

                    rowHash[i].add(board[i][j])
                    colHash[j].add(board[i][j])
                    square[(newRow, newCol)].add(board[i][j])
                    if solve(ind + 1):
                        return True
                    rowHash[i].remove(board[i][j])
                    colHash[j].remove(board[i][j])
                    square[(newRow, newCol)].remove(board[i][j])
                    board[i][j] = '.'
            return False
        solve(0)