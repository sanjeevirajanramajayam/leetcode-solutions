class Solution:
    def numSquares(self, n: int) -> int:
        @cache
        def fn(n):
            if n <= 0:
                return 0
            # print(n)
            mini = float('inf')
            i = 1
            while i * i <= n:
                mini = min(1 + fn(n - (i * i)), mini) 
                i += 1
            return mini
        
        return fn(n)