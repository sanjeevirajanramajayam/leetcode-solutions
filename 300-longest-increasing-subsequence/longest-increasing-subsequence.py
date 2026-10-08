class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        arr = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    arr[i] = max(arr[i], arr[j] + 1)
        return max(arr)
        