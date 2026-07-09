class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)
        ans = float('inf')
        @cache
        def fn(ind, score):
            nonlocal ans
            if ind == len(s):
                ans = min(ans, score)
            temp = ""
            for i in range(ind, len(s)):
                temp += s[i]
                if temp in dictionary:
                    fn(i + 1, score)
                else:
                    fn(i + 1, score + (i - ind) + 1)

        fn(0, 0)
        return ans