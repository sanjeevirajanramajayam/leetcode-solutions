class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        dp = [[0 for i in range(COLS)] for i in range(ROWS)]
        for i in range(ROWS):
            if matrix[i][0] == 1:
                dp[i][0] = 1
        for  j in range(COLS):
            if matrix[0][j] == 1:
                dp[0][j] = 1 
        # print(dp)
        for i in range(1, ROWS):
            for j in range(1, COLS):
                if matrix[i][j] == 1:
                    t = dp[i - 1][j] if i - 1 >=0 and i - 1 < ROWS and j >= 0 and j < COLS else float('inf')
                    l = dp[i][j - 1] if i >=0 and i < ROWS and j - 1 >= 0 and j - 1 < COLS else float('inf')
                    tl = dp[i - 1][j - 1] if i - 1 >=0 and i - 1 < ROWS and j - 1 >= 0 and j - 1 < COLS else float('inf')
                    mini = min(t, l , tl)
                    dp[i][j] += mini + 1
        # print(dp)
        return sum([sum(x) for x in dp])