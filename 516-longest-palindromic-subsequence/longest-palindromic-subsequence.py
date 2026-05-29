class Solution:
    def longestPalindromeSubseq(self, text1: str) -> int:
        # code here
        text2 = text1[::-1]
        dp = [[-1 for i in range(len(text2) + 1 )] for j in range(len(text1) + 1 )]

        for i in range(len(text1) + 1):
            dp[i][0] = 0
        for i in range((len(text2) + 1)):
            dp[0][i] = 0
        
        for i in range(1, len(text2) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    continue
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])


        return dp[len(text1)][len(text2)]