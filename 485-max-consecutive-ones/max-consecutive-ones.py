class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxCount = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                maxCount = max(maxCount, count)
                count = 0
        maxCount = max(maxCount, count)
        return maxCount