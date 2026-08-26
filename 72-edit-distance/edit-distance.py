class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def fn(i, j):
            if i < 0:
                return j + 1 # insert word2 rem chars
            if j < 0:
                return i + 1 # delete word1 rem chars
            if word1[i] == word2[j]:
                return fn(i-1, j - 1)
            # insert
            return min(1 + fn(i - 1, j - 1), 1 + fn(i-1, j), 1 + fn(i,j-1))
        return fn(len(word1) - 1, len(word2) - 1)