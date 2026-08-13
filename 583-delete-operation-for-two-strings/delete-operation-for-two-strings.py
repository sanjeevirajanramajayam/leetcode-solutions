class Solution:
    def minDistance(self, s: str, s2: str) -> int:
        dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s) + 1)]
        for i in range(1, len(s) + 1):
            for j in range(1, len(s2) + 1):
                if s[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][ j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j ])
        
        return len(s) + len(s2) + - 2* dp[len(s)][len(s2)]