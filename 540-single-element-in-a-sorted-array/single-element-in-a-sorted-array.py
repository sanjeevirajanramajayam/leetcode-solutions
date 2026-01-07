class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums) - 1

        if len(nums) == 1:
            return nums[0]

        if nums[0] != nums[1]:
            return nums[0]
        
        if nums[len(nums) - 1] != nums[len(nums) - 2]:
            return nums[len(nums) - 1]

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            if (nums[mid] == nums[mid + 1] and mid % 2 == 0) or (nums[mid] == nums[mid - 1] and mid % 2 != 0):
                low = mid + 1
            else:
                high = mid - 1