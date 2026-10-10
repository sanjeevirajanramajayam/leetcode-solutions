class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        #lcs
        dp = [[0 for i in range(len(str2) + 1)] for i in range(len(str1) + 1)]

        for i in range(len(str1), -1, -1):
            for j in range(len(str2), -1, -1):
                if i == len(str1):
                    dp[i][j] = 0
                    continue

                if j == len(str2):
                    dp[i][j] = 0
                    continue

                if str1[i] == str2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        # for x in dp:
            # print(x)
        i = 0
        j = 0
        ans = ""
        while i < len(str1) and j < len(str2):
            # print(i, j, str1[i], str2[j])
            if str1[i] == str2[j]:
                ans += str1[i]
                i += 1
                j += 1
            elif dp[i + 1][j] > dp[i][j + 1]:
                ans += str1[i]
                i += 1
            else:
                ans += str2[j]
                j += 1
        while i < len(str1):
            ans += str1[i]
            i += 1
        while j < len(str2):
            ans += str2[j]
            j += 1
        return ans
        # return dp[0][0]

