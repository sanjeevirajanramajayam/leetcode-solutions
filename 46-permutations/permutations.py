class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = [0] * len(nums)
        ans = []
        def fn(ind, arr):
            if ind == len(nums):
                ans.append(arr[:])
                return 
            for i in range(len(visited)):
                if visited[i] == 0:
                    visited[i] = 1
                    fn(ind + 1, arr + [nums[i]])
                    visited[i] = 0
        fn(0, [])
        return ans