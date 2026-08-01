class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = len(nums) - 1
        currSum = 0
        maxLen = float('-inf')
        for r in range(len(nums) - 1, -1, -1):
            currSum += nums[r]
            # print(currSum, r)
            while currSum + k < (l - r + 1) * nums[l]:
                currSum -= nums[l]
                l -= 1
            # print(currSum + k, l, r, (l - r + 1) * nums[l])
            maxLen = max(maxLen, (l - r + 1))
        return maxLen
