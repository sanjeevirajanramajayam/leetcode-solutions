class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        front = [0, 0]
        curr = [-1, -1]

        for ind in range(len(prices) - 1, -1, -1):
            for buy in range(2):
                if buy == 0:
                    curr[buy] = max(-prices[ind] + front[ 1], front[0])
                else:
                    curr[buy] = max(prices[ind] + front[0], front[1])
            front = curr[:]
        return curr[0]