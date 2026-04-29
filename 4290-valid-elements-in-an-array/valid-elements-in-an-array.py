class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        max_vl = -1
        valid = set()
        for i in range(len(nums)):
            if nums[i] > max_vl:
                max_vl = nums[i]
                valid.add(i)
        max_vl = -1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > max_vl:
                max_vl = nums[i]
                valid.add(i)
        return [nums[i]   for i in range(len(nums)) if i in valid]
        print(valid)