class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        count = [1] * len(nums)
        dp = [1] * len(nums)
        maxi = float('-inf')
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]
        maxi = max(dp)

        nos = 0
        for i in range(len(nums)):
            if dp[i] == maxi:
                nos += count[i]
        return nos