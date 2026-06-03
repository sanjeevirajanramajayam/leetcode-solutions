class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for x in range(n)] for j in range(n)]
        ans = []
        def isSafe(row, col):
            # print(row, col)
            # upper diagonal
            trow = row
            tcol = col
            while trow >= 0 and tcol >= 0:
                # print(trow, tcol, board[trow])
                if board[trow][tcol] == 'Q':
                    return False
                trow -= 1
                tcol -= 1
            
            for i in range(n):
                if board[row][i] == 'Q':
                    return False
            
            trow = row
            tcol = col
            while trow < n and tcol >= 0:
                if board[trow][tcol] == 'Q':
                    return False
                trow += 1
                tcol -= 1
            return True

                
        def fn(col):
            print(col)
            if col == n:
                ans.append([x[:] for x in board[:]])
                return 
            for row in range(n):
                if isSafe(row, col):
                    board[row][col] = 'Q'
                    fn(col + 1)
                    board[row][col] = '.'
        fn(0)
        for x in ans:
            for j in range(len(x)):
                x[j] = "".join(x[j])
            #     print(x[j])
            # print()
        return ans