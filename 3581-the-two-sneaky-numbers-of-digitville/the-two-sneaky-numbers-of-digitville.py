class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq_arr = [0] * 101
        ans = []
        for i in range(len(nums)):
            freq_arr[nums[i]] += 1
            if freq_arr[nums[i]] == 2:
                ans.append(nums[i])
            if len(ans) == 2:
                break
        return ans
