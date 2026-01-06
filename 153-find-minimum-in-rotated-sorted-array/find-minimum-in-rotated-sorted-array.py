class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        min_index = 0
        while low <= high:
            mid = (low + high) // 2
            if nums[low] <= nums[mid]:
                if nums[min_index] > nums[low]:
                    min_index = low
                low = mid + 1
            else:
                if nums[min_index] > nums[mid]:
                    min_index = mid
                high = mid - 1
        return nums[min_index]