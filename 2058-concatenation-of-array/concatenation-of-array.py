class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums2 = []
        for i in nums:
            nums2.append(i)
        for i in nums:
            nums2.append(i)
        return nums2