class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l = 0
        r = 1
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r += 1
                continue
            if r >= len(prices):
                break
            maxProfit = max(maxProfit, prices[r] - prices[l])
            r += 1
        return maxProfit