class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        def fn(ind, arr):
            nonlocal ans
            if ind == len(nums):
                xor = 0
                for i in arr[:]:
                    xor ^= i
                ans += xor
                return
            fn(ind + 1, arr)
            fn(ind + 1, arr + [nums[ind]])
        fn(0, [])
        return ans