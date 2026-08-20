class Solution:
    def numSquares(self, n: int) -> int:
        @cache
        def fn(target):
            print(target)
            if target == 0:
                return 0
            if target == 1:
                return 1
            i = 1
            ans = float('inf')
            while i * i <= target:
                ans = min(ans, 1 + fn(target - (i * i)))
                i += 1
            return ans
        return fn(n)