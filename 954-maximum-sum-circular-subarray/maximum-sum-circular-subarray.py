class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currSum1 = 0
        currSum2 = 0
        maxSum = float('-inf')
        minSum = float('inf')

        for i in range(len(nums)):
            currSum1 += nums[i]
            currSum2 += nums[i]

            maxSum = max(maxSum, currSum1)
            minSum = min(currSum2, minSum)

            if currSum1 < 0:
                currSum1 = 0
            
            if currSum2 > 0:
                currSum2 = 0
        # print(maxSum , minSum)
        if minSum == sum(nums):
            return maxSum
        return max(maxSum, sum(nums) - minSum)