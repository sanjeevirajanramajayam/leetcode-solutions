class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] != val:
                # swap
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1
            j += 1
        # print(nums)
        return i 