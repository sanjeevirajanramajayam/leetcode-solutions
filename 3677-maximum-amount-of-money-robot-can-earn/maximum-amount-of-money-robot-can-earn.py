from math import inf

class Solution:
    def maximumAmount(self, coins):
        ROWS = len(coins)
        COLS = len(coins[0])

        dp = [[[-inf] * 3 for _ in range(COLS)]
              for _ in range(ROWS)]

        for k in range(3):
            if coins[-1][-1] < 0 and k > 0:
                dp[-1][-1][k] = 0
            else:
                dp[-1][-1][k] = coins[-1][-1]

        for i in range(ROWS - 1, -1, -1):
            for j in range(COLS - 1, -1, -1):

                if i == ROWS - 1 and j == COLS - 1:
                    continue

                for k in range(3):

                    best = -inf

                    if j + 1 < COLS:
                        best = max(
                            best,
                            coins[i][j] + dp[i][j + 1][k]
                        )

                        if coins[i][j] < 0 and k > 0:
                            best = max(
                                best,
                                dp[i][j + 1][k - 1]
                            )

                    if i + 1 < ROWS:
                        best = max(
                            best,
                            coins[i][j] + dp[i + 1][j][k]
                        )

                        if coins[i][j] < 0 and k > 0:
                            best = max(
                                best,
                                dp[i + 1][j][k - 1]
                            )

                    dp[i][j][k] = best

        return dp[0][0][2]