class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)

        minVal = float('inf')
        for i in range(len(nums) - (k - 1)):
            # print(i, i + k - 1, nums[i], nums[i + k - 1])
            minVal = min(nums[i + k - 1] - nums[i], minVal)
        return minVal

