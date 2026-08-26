class Solution:
    def jump(self, nums: List[int]) -> int:
        l = 0
        r = 0
        res = 0
        while r < len(nums) - 1:
            furtherest = r
            for i in range(l, r+ 1):
                furtherest = max(furtherest, i + nums[i])
            l = r + 1
            r = furtherest
            res += 1
        return res