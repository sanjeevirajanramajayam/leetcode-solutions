class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n + 1)
        
        def f(n):
            if n <= 1:
                return 1
            # print(n)
            if dp[n] != -1:
                return dp[n]
            
            dp[n] = f(n - 1) + f(n - 2)
            return dp[n]
        
        return f(n)