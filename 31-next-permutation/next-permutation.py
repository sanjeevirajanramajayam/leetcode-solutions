class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def reverse(start, end, array):
            while start < end:
                temp = array[start]
                array[start] = array[end]
                array[end] = temp
                start += 1
                end -= 1
                
        ind = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                ind = i
                break
        
        if ind == -1:
            reverse(0, len(nums) - 1, nums)
            return
        
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > nums[ind]:
                temp = nums[i]
                nums[i] = nums[ind]
                nums[ind] = temp
                break


        
        reverse(ind + 1, len(nums) - 1, nums)
