class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def lessThanK(k):
            subCount = 0
            oddCount = 0
            l = 0

            for r in range(len(nums)):
                if nums[r] % 2 != 0:
                    oddCount += 1

                while oddCount > k:
                    if nums[l] % 2 != 0:
                        oddCount -= 1
                    l += 1
                
                if oddCount <= k:
                    subCount += (r - l + 1)
            return subCount
        return lessThanK(k) - lessThanK(k - 1)
