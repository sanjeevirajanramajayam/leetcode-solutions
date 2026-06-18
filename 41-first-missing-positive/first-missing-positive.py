class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        j = 0
        while j < len(nums) and nums[j] <= 0:
            j += 1
        cnt = 1
        for i in range(j, len(nums)):
            if cnt != nums[i]:
                return cnt
            cnt += 1
        return cnt