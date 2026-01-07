class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return 0

        if nums[0] > nums[1]:
            return 0

        if nums[len(nums) - 1] > nums[len(nums) - 2]:
            return len(nums) - 1
        
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = ( low + high ) // 2
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            if nums[mid] > nums[mid + 1]:
                high = mid - 1
            else:
                low = mid + 1