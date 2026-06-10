class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        ans = []
        def fn(ind, s):
            if ind == len(digits):
                ans.append(s[:])
                return
            for char in letters[digits[ind]]:
                fn(ind + 1, s + char)
        fn(0, "")
        return ans