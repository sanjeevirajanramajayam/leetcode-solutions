class Solution(object):
    def minRemoval(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = 0
        r = 0
        nums = sorted(nums)
        minElements = float('inf')

        if len(nums) == 1:
            return 0

        while r < len(nums) - 1:
            # print(l, r)
            while nums[r + 1] <= nums[l] * k:
                r += 1
                # print(r)
                if r == len(nums) - 1:
                    break
            minElements = min(minElements, len(nums) - (r - l + 1))
            # print(l, r)
            l += 1
            # print(l, r)
                
        return (minElements)