class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)
        n = len(s)
        @cache
        def fn(ind):
            if ind == n:
                return 0
            
            mini = 1 + fn(ind + 1)
            for i in range(ind, n):
                if s[ind:i + 1] in dictionary:
                    mini = min( mini , fn(i + 1))

            return mini

        return fn(0)