class Solution:
    def minCut(self, s: str) -> int:
        @cache
        def fn(i):
            if i == len(s):
                return 0
            ans = float('inf')
            temp = ""

            for j in range(i,  len(s)):
                temp += s[j]
                if temp == temp[::-1]:
                    ans = min(ans, 1 + fn(j + 1))
            return ans 
        return fn(0) - 1
