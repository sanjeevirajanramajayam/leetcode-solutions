class Solution:
    def findTargetSumWays(self, arr: List[int], target: int) -> int:
        totSum = sum(arr)
        dp = [[-1 for i in range((totSum - target) // 2 + 1)] for j in range(len(arr))]

        def fn(ind, target):
            if ind == 0:
                if target == 0 and arr[ind] == 0:
                    return 2
                if target == 0 or target == arr[ind]:
                    return 1
                return 0
            if dp[ind][target] != -1:
                return dp[ind][target]
            take = 0
            if arr[ind] <= target:
                take = fn(ind - 1, target - arr[ind])
            not_take = fn(ind - 1, target)
            dp[ind][target] = take + not_take
            return take + not_take
        totSum = sum(arr)
        if ( totSum - target < 0 or (totSum - target) % 2 != 0):
            return 0
        
        return fn(len(arr) - 1, (totSum - target) // 2)
        '''
        s1 - s2 = target
        s2 = totSum - target / 2
        '''
        