class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def fn(i, j):
            if j < 0:
                return 1
            if i < 0:
                return 0

            if s[i] == t[j]:
                return fn(i - 1, j - 1) + fn(i - 1, j)
            else:
                return fn(i - 1, j)
        return fn(len(s) - 1, len(t) - 1)
