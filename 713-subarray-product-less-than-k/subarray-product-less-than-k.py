class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        cnt = 0
        l = 0
        currProd = 1
        for r in range(len(nums)):
            currProd *= nums[r]
            while l < len(nums) and currProd >= k:
                currProd /= nums[l]
                l += 1
            cnt += r - l + 1
        return cnt