class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [['.' for x in range(n)] for x in range(n)]
        rows = set()
        bottomRight = set()
        topRight = set()

        def isSafe(row, col):
            if row in rows:
                return False
            
            if row + col in bottomRight:
                return False
            
            if row - col in topRight:
                return False
            
            return True
        cnt = 0
        def fn(col):
            nonlocal cnt
            if col == n:
                cnt += 1
                return 
            
            for row in range(n):
                if isSafe(row, col):
                    board[row][col] = 'Q'
                    rows.add(row)
                    bottomRight.add(row + col)
                    topRight.add(row - col)
                    fn(col + 1)
                    board[row][col] = '.'
                    rows.remove(row)
                    bottomRight.remove(row + col)
                    topRight.remove(row - col)
        fn(0)
        return cnt