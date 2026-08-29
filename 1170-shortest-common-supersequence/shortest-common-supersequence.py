class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        dp = [[0 for i in range(len(str2) + 1)] for i in range(len(str1) + 1)]
        
        for i in range(1, len(str1) + 1):
            for j in range(1, len(str2) + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        for x in dp:
            print(x)
        
        i = len(str1)
        j = len(str2)
        ans = ""

        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                ans += str1[i - 1]
                i -= 1
                j -= 1
            elif dp[i][j - 1] > dp[i - 1][j]:
                ans += str2[j - 1]
                j -= 1
            else:
                ans += str1[i - 1]
                i -= 1
        
        while i > 0:
            ans += str1[i - 1]
            i -= 1
         
        while j > 0:
            ans += str2[j - 1]
            j -= 1
        
        return ans[::-1]