class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[-1 for j in range(amount + 1)] for i in range(len(coins))]
        def fn(ind, curr):
            if ind == 0:
                if curr % coins[ind] == 0:
                    return curr // coins[ind]
                else:
                    return float('inf')
            if dp[ind][curr] != -1:
                return dp[ind][curr]
            take = float('inf')
            if coins[ind] <= curr:
                take = 1 + fn(ind, curr - coins[ind])
            not_take = fn(ind - 1, curr)
            dp[ind][curr] = min(take, not_take)
            return min(take, not_take)
        ans = fn(len(coins) - 1, amount)
        if ans == float('inf'):
            return -1
        return ans