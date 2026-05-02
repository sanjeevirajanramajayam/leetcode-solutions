class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        i = len(nums) - 1
        while i >= 0 and nums[i] <= nums[i - 1]:
            i -= 1
        # print(i, nums[i])
        if i == 0:
            nums.reverse()
            # print(nums)
            return
        prevPivot = i - 1
        pivot = i
        for i in range(len(nums) - 1, pivot - 1, -1):
            # print(nums[i], nums[prevPivot])
            if nums[i] > nums[prevPivot]:
                temp = nums[i]
                nums[i] = nums[prevPivot]
                nums[prevPivot] = temp
                nums[prevPivot + 1:] = nums[prevPivot + 1:][::-1]
                break
        