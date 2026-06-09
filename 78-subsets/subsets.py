class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def fn(ind, arr):
            if ind == len(nums):
                ans.append(tuple(arr[:]))
                return
            fn(ind + 1, arr)
            fn(ind + 1, arr + [nums[ind]])
        fn(0, [])
        return ans