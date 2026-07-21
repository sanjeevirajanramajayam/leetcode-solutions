class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        minSum = float('inf')
        minCurrSum = 0
        maxCurrSum = 0

        for i in nums:
            minCurrSum += i
            maxCurrSum += i
            maxSum = max(maxSum, maxCurrSum)
            minSum = min(minSum, minCurrSum)
            if maxCurrSum < 0:
                maxCurrSum = 0
            if minCurrSum > 0:
                minCurrSum = 0
        # print(maxSum, minSum)
        if (sum(nums) - minSum) == 0:
            return maxSum
        return max(maxSum, (sum(nums) - minSum))
            
