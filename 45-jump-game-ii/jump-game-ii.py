class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = 0
        jumps = 0
        while r < (len(nums) - 1):
            furthest = float('-inf')
            for i in range(l, r + 1):
                furthest = max(furthest, i + nums[i])
            l = r + 1
            r = furthest
            jumps += 1
        return jumps