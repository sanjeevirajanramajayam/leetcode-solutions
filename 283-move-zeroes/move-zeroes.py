class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = 1
        while l<len(nums) and r < len(nums):
            # print(l, r, nums)
            if nums[l] == 0:
                while r < len(nums) and nums[r] == 0:
                    r += 1
                # print(l, r)
                if r >= len(nums):
                    break
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                # print(nums, nums[l], nums[r])
            l += 1 
            r += 1