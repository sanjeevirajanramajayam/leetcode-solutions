class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        suffix = 1
        prefix = 1
        maxProd = float('-inf')
        for i in range(len(nums)):
            prefix *= nums[i]
            j = len(nums) - 1 - i
            suffix *= nums[j]
            maxProd = max(maxProd, suffix, prefix)
            if suffix == 0:
                suffix = 1
            if prefix == 0:
                prefix = 1
        return maxProd
            
        