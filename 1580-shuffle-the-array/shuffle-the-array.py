class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        length = len(nums)
        nums2 = []
        for i in range(n):
            nums2.append(nums[i])
            nums2.append(nums[i + n])
        return nums2