class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def fn(ind, target):
            
            if ind == 0:
                if target % coins[ind] == 0:
                    return 1
                else:
                    return 0
            take = 0
            if target >= coins[ind]:
                take = fn(ind, target - coins[ind])
                # print(coins[ind], take - 1, 1)
            not_take = fn(ind - 1, target)
            # print(take, not_take)

            return take + not_take

        x = fn(len(coins) - 1, amount) 

        if x == float('inf'):
            return -1

        return x