class Solution(object):
    def longestBalanced(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLen = 0
        for i in range(0, len(nums)):
            evenSet = set()
            oddSet = set()
            for j in range(i, len(nums)):
                if nums[j] % 2 == 0:
                    evenSet.add(nums[j])
                else:
                    oddSet.add(nums[j])
                
                if len(evenSet) == len(oddSet):
                    maxLen = max(maxLen, j - i + 1)
        return maxLen
                
