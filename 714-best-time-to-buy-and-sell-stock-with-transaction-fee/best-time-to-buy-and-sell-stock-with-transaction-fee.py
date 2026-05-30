class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [[-1] * 2 for i in range(len(prices) + 1) ]
        def fn(ind, buy):
            if ind >= len(prices):
                return 0
            if dp[ind][buy] != -1:
                return dp[ind][buy]
            if buy == 0:
                dp[ind][buy] = max(-prices[ind] - fee + fn(ind + 1, 1), fn(ind + 1, 0))
                return dp[ind][buy]
            else:
                dp[ind][buy] = max(prices[ind] + fn(ind + 1, 0), fn(ind + 1, 1))
                return dp[ind][buy]
        return fn(0, 0)