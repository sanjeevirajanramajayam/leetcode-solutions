class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def fn(i, j):
            if i < 0 or j < 0:
                return 0
            maxi = float('-inf')
            if text1[i] == text2[j]:
                maxi = 1 + max(maxi, fn(i - 1, j - 1))
            else:
                maxi = max(maxi, fn(i - 1, j), fn(i, j - 1))
            
            return maxi
        return fn(len(text1) - 1, len(text2) - 1 )