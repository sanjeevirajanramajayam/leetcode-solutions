class Solution:
    def maxArea(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1
        maxArea = 0
        while l < r:
            if nums[r] > nums[l]:
                maxArea = max(maxArea, min(nums[r], nums[l]) * (r - l))
                l += 1
            else:
                maxArea = max(maxArea, min(nums[r], nums[l]) * (r - l))
                r -= 1
        return maxArea