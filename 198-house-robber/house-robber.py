class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        def fn(ind):
            if ind == 0:
                return nums[ind]
            if ind < 0:
                return 0
            if dp[ind] != -1:
                return dp[ind]
            take = fn(ind - 2) + nums[ind]
            not_take = fn (ind - 1)
            dp[ind] = max(take, not_take)
            return dp[ind]
        
        return fn(len(nums) - 1)