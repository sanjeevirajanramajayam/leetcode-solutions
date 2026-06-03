class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visited = [0 for i in range(len(nums))]
        def fn(ind, arr):
            # print(ind, arr)
            if ind == len(nums):
                ans.append(arr[:])
                return 

            for i in range(len(nums)):
                if visited[i] == 0:
                    visited[i] = 1
                    fn(ind + 1, arr + [nums[i]])
                    visited[i] = 0
        fn(0, [])
        return ans