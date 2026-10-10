class Solution:
    def longestArithSeqLength(self, nums: list[int]) -> int:
        dp = [{} for i in range(len(nums))]
        longest = float('-inf')
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] = dp[j].get(diff, 1) + 1
                longest = max(longest, dp[i][diff])
        # print(dp)
        return longest