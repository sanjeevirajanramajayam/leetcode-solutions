class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for i in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        maxi = float('-inf')
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    maxi = max(maxi, dp[i][j])
                else:
                    # print(i, j, len(dp), len(dp[0]))
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    maxi = max(maxi, dp[i][j])

        # print(dp)
        # for x in dp:
            # print(x)
        return maxi