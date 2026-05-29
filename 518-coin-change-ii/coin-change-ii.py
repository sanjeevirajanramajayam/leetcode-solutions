class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1 for i in range(amount + 1)] for i in range(len(coins))]
        def fn(ind, target):
            if ind == 0:
                return 1 if target % coins[0] == 0 else 0
            if dp[ind][target] != -1:
                return dp[ind][target]  
            take = 0
            if target >= coins[ind]:
                take = fn(ind, target - coins[ind])
            not_take = fn(ind - 1, target)
            dp[ind][target] = take + not_take
            return take + not_take
        return fn(len(coins) - 1, amount)