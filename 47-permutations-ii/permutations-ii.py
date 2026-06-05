class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        visited = [0] * len(nums)
        ans = set()
        def fn(ind, arr):
            if ind == len(nums):
                ans.add(tuple(arr[:]))
                return 
            for i in range(len(visited)):
                if visited[i] == 0:
                    visited[i] = 1
                    fn(ind + 1, arr + [nums[i]])
                    visited[i] = 0
        fn(0, [])
        return [list(x) for x in ans]