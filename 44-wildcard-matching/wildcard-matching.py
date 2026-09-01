class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def fn(i, j):
            if i < 0:
                for k in range(0, j + 1):
                    if p[k] != '*':
                        return False
                return True

            if j < 0:
                return i < 0
            

            if s[i] == p[j]:
                return fn(i - 1, j - 1)
            elif p[j] == '?':
                return fn(i - 1, j - 1)
            elif p[j] == '*':
                return fn(i, j - 1) or fn(i - 1, j)
            else:
                return False
        
        return fn(len(s) - 1, len(p) - 1)