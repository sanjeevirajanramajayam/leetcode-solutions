class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        @cache
        def fn(ind, r):
            if ind >= r:
                return 0
            
            take = nums[ind] + fn(ind + 2, r)
            not_take = fn(ind + 1, r)

            return max(take, not_take)
        return max(fn(0, len(nums) - 1), fn(1, len(nums)))