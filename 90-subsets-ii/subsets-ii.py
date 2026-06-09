class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def fn(start, arr):
            ans.append(arr[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                fn(i + 1, arr + [nums[i]])
        fn(0, [])
        return ans