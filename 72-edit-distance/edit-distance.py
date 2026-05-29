class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[-1 for i in range(len(word2))] for i in range(len(word1))]
        def fn(ind1, ind2):
            if ind1 < 0:
                return ind2 + 1
            if ind2 < 0:
                return ind1 + 1
            if dp[ind1][ind2] != -1:
                return dp[ind1][ind2]
            
            if word1[ind1] == word2[ind2]:
                return fn(ind1 - 1, ind2 - 1)
            
            dp[ind1][ind2] =  1 + min(fn(ind1, ind2 - 1), # insert
            fn(ind1 - 1, ind2),
            fn(ind1 - 1, ind2 - 1))
            return dp[ind1][ind2]
        return fn(len(word1) - 1, len(word2) - 1)
