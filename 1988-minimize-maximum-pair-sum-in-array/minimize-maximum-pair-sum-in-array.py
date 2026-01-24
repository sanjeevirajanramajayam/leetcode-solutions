class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        l = 0
        r = len(nums) - 1
        maxSum = 0
        while nums[l] <= nums[r]:
            maxSum = max(maxSum, nums[l] + nums[r])
            l += 1
            r -= 1
        return maxSum
            
