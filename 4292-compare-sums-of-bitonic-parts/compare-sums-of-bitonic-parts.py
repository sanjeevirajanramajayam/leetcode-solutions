class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        i = 0
        leftSum = 0
        n = len(nums)
        while i < n and nums[i+1] > nums[i]:
            leftSum += nums[i]
            i += 1
        peak = i
        leftSum += nums[i]
        rightSum = 0
        while i < n - 1 and nums[i + 1] < nums[i]:
            rightSum += nums[i]
            i += 1
        rightSum += nums[i]
        # print()
        if leftSum > rightSum:
            return 0
        elif rightSum > leftSum:
            return 1
        else:
            return -1