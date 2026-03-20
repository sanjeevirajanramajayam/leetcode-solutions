class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leftProd = [1 for i in range(len(nums) + 1)]
        rightProd = [1 for i in range(len(nums) + 1)]

        for i in range(1, len(leftProd)):
            leftProd[i] = leftProd[i - 1] * nums[i - 1]
    
        for i in range(len(nums) - 2, -1, -1):
            # print(i + 1)
            rightProd[i] = rightProd[i + 1] * nums[i + 1]
        
        ans = []
        for i in range(len(nums)):
            # print(leftProd[i], rightProd[i])
            ans.append(leftProd[i] * rightProd[i])
        return ans