class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)
        @cache
        def fn(ind):
            mini = float('inf')
            if ind == len(s):
                return 0
            skipped = 1 + fn(ind + 1)
            mini = min(mini, skipped)
            for i in range(ind, len(s)):
                if s[ind:i + 1] in dictionary: 
                    mini = min(mini, fn(i + 1))
            return mini
        return fn(0)