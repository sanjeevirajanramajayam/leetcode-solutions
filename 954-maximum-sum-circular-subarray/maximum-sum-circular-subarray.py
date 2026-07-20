class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxAns = float('-inf')
        currSum = 0
        cnt = 0
        for i in nums:
            currSum += i
            if currSum > maxAns:
                maxAns = currSum
            if currSum < 0:
                currSum = 0
        
        minAns = float('inf')
        currSum = 0
        cnt = 0
        for i in nums:
            currSum += i
            if currSum < minAns:
                minAns = currSum
            if currSum > 0:
                currSum = 0
        # print(maxAns, minAns)
        if (sum(nums) - minAns) == 0:
            return maxAns
        return max(maxAns, sum(nums) - minAns)