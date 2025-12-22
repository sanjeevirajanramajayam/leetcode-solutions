class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(nums)
        stack = []
        n = len(nums)
        for i in range(2 * len(nums) - 1, -1, -1):
            while stack and stack[-1] <= nums[i % n]:
                stack.pop()
            if not stack and i < len(nums):
                ans[i] = -1
            elif i < len(nums):
                ans[i] = stack[-1]
            stack.append(nums[i % n])
        return ans
            

