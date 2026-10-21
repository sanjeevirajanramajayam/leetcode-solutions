class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        dp = [0] * len(nums)
        cnt = 0
        for i in range(2, len(nums)):
            if nums[i - 1] - nums[i - 2] == nums[i] - nums[i - 1]:
                dp[i] = dp[i - 1] + 1
            cnt += dp[i]
        return cnt