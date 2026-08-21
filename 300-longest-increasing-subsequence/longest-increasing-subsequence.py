class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # maxi = float('-inf')
        dp = [1 for i in range(len(nums))]

        for i in range(len(nums) + 1):
            for j in range(1, i):
                # print(i - 1, j - 1, nums[j - 1], nums[i - 1])
                if nums[j - 1] < nums[i - 1]:
                    dp[i - 1] = max(dp[i - 1], dp[j - 1] + 1)
        # print(dp)
        return max(dp)