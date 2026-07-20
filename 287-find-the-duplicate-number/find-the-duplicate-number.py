class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            # print(nums[i], nums[abs(nums[i])])
            if nums[abs(nums[i])] < 0:
                return abs(nums[i])
            nums[abs(nums[i])] = -nums[abs(nums[i])]