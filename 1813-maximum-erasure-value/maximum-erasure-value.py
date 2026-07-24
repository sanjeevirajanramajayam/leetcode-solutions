class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0
        # r = 0
        hash = {}
        currSum = 0
        maxSum = float('-inf')
        for r in range(len(nums)):
            hash[nums[r]] = hash.get(nums[r], 0) + 1
            currSum += nums[r]
            while hash[nums[r]] > 1:
                hash[nums[l]] -= 1
                currSum -= nums[l]
                if hash[nums[l]] == 0:
                    del hash[nums[l]]
                l += 1
            # print(hash)
                # print(hash)
            maxSum = max(maxSum, currSum)
        if maxSum == float('-inf'):
            return 0
        return maxSum