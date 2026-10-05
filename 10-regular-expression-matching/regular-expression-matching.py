class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def fn(i, j):
            if j == len(p):
                return i == len(s)
            
            first_match = i < len(s) and( s[i] == p[j] or p[j] == '.')

            if j + 1 < len(p) and p[j + 1] == '*':
                return ((first_match and fn(i + 1, j)) or  fn(i, j + 2))
            else:
                return (first_match) and fn(i + 1, j + 1)

        return fn(0, 0)