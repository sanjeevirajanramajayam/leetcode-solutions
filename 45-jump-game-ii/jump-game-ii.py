class Solution:
    def jump(self, nums: list[int]) -> int:
        l = 0
        r = nums[0]
        if len(nums) == 1:
            return 0
        jumps = 1
        while r < len(nums) - 1:
            # print(l, r)
            newR = r
            for k in range(l, r + 1):
                # print("k + ", k + nums[k])
                newR = max(newR, k + nums[k])
            # print("newR", newR)
            jumps += 1
            l = r
            r = newR
            # print(l, r)
        return jumps