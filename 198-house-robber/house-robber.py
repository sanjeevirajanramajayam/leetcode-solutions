class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def fn(ind):
            if ind >= len(nums):
                return 0
            
            take = nums[ind] + fn(ind + 2)
            not_take = fn(ind + 1)

            return max(take, not_take)
        return fn(0)
