class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = {}
        ans = []
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
            if freq[nums[i]] == 2:
                ans.append(nums[i])
            if len(ans) == 2:
                break
        return ans
