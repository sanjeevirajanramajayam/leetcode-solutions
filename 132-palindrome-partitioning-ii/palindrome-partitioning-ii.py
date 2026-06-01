class Solution:
    def minCut(self, s: str) -> int:
        if s == s[::-1]:
            return 0
        dp = {}
        def fn(i):
            if i == len(s):
                return 0
            if i in dp:
                return dp[i]
            temp = ""
            mini = float('inf')
            for j in range(i, len(s)):
                temp += s[j]
                if temp == temp[::-1]:
                    mini = min(mini, 1 + fn(j + 1))
            dp[i] = mini
            return mini
        return fn(0) - 1