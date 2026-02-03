class Solution(object):
    def isTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = 0
        p = -1
        q = -1

        n = len(nums)
        while i < n - 1 and nums[i] < nums[i + 1]:
            i += 1

        p = i

        if not (0 < p and p < len(nums) - 1):
            return False

        while i < n - 1 and nums[i] > nums[i + 1]:
            i += 1
        
        q = i

        if not (0 < q and q < len(nums) - 1 and q > p):
            return False

        while i < n - 1 and nums[i] < nums[i + 1]:
            i += 1
        
        # print(i)
        if i != len(nums) - 1:
            return False
        else:
            return True


