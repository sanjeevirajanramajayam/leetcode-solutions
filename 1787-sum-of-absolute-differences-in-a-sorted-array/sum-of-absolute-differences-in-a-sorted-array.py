class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefixSum = [0 for i in range(len(nums) + 1)]
        suffixSum = [0 for i in range(len(nums) + 1)]

        for i in range(len(nums)):
            prefixSum[i + 1] = prefixSum[i] + nums[i]

        for i in range(len(nums) - 1, -1, -1):
            suffixSum[i - 1] = suffixSum[i] + nums[i]
            # print(suffixSum)
        # print(prefixSum, suffixSum)
        ans = []
        for i in range(len(nums)):
            rightSum = suffixSum[i] - ((len(nums) - 1 - i) * nums[i])
            leftSum = (i * nums[i]) - prefixSum[i]
            ans.append(rightSum + leftSum)
        
        return ans