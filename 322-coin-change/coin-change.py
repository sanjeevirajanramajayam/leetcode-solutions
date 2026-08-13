class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def fn(ind, target):
            # print(ind, target)
            if target == 0:
                return 0
            
            if ind == 0:
                if target % coins[ind] == 0:
                    return target // coins[ind]
                else:
                    return float('inf')
            take = float('inf')
            if target >= coins[ind]:
                take = 1 + fn(ind, target - coins[ind])
                # print(coins[ind], take - 1, 1)
            not_take = fn(ind - 1, target)

            return min(take, not_take)
        x = fn(len(coins) - 1, amount) 
        if x == float('inf'):
            return -1
        return x