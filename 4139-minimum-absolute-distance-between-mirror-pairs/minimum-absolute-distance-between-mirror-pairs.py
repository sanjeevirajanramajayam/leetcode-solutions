class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse(num):
            rev = 0
            while num > 0:
                rev = (rev * 10) + num % 10
                num //= 10
            return rev
        mirrorMap = {}
        ans = float('inf')
        for i in range(len(nums)):
            # rev = reverse(nums[i])
            if nums[i] in mirrorMap:
                ans = min(ans, abs(i - mirrorMap[nums[i]]))
            mirrorMap[reverse(nums[i])] = i
        if ans == float('inf'):
            return -1
        return ans