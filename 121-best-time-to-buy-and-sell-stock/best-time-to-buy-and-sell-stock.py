class Solution:
    def maxProfit(self, nums: list[int]) -> int:
        l = 0
        maxProfit = 0 
        for r in range(len(nums)):
            maxProfit = max(maxProfit, nums[r] - nums[l])
            if nums[r] < nums[l]:
                l = r 
        return maxProfit