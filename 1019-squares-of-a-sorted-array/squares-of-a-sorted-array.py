class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        ret = []
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                ret.append( nums[l] * nums[l])
                l += 1
            else:
                ret.append(nums[r] * nums[r])
                r -= 1
        return ret[::-1]