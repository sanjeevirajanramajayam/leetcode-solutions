class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[[-1] * 3 for _ in range(2)] for _ in range(len(prices))]
        def fn(ind, buy, cap):
            if ind == len(prices):
                return 0
            if cap == 2:
                return 0
            if dp[ind][buy][cap] != -1:
                return dp[ind][buy][cap]
            if buy == 0:
                dp[ind][buy][cap] = max(-prices[ind] + fn(ind + 1, 1, cap), fn(ind + 1, 0, cap))
                return dp[ind][buy][cap]
            else:
                dp[ind][buy][cap] =  max(prices[ind] + fn(ind + 1, 0, cap + 1), fn(ind + 1, 1, cap))
                return dp[ind][buy][cap]
        return fn(0,0,0)