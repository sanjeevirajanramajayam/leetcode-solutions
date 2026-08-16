class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        maxi = 1
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    # print(nums[i], nums[j])
                    dp[i] = max(dp[i], dp[j] + 1)
                    maxi = max(dp[i], maxi)
        # print(dp)
        return maxi