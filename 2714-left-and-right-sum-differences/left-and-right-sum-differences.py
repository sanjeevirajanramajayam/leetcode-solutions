class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rightSum = sum(nums) - nums[0]
        ans = [abs(rightSum)]
        left = nums[0]
        for i in range(1, len(nums)):
            rightSum -= nums[i]
            ans.append(abs(rightSum - left))
            left += nums[i]
        return ans
