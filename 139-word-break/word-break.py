class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dictionary = set(wordDict)
        @cache
        def fn(ind):
            if ind == len(s):
                return True
            for i in range(ind, len(s)):
                if s[ind:i + 1] in dictionary: 
                    if fn(i + 1) is True:
                        return True
            return False
        return fn(0)