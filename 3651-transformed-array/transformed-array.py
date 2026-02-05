class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)):
            if nums[i] == 0:
                result.append(nums[i])
            elif nums[i] > 0:
                result.append(nums[(i + nums[i]) % len(nums)])
            else:
                sub = i - abs(nums[i])
                if sub < 0:
                    sub += len(nums)
                sub = sub % len(nums)
                result.append(nums[sub])
        return result