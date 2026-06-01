class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}
        def fn(i, j):
            if i > j:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            mini = float('-inf')
            for k in range(i, j + 1):
                mini = max(mini, fn(i, k - 1) + fn(k + 1, j) + nums[k] * nums[i - 1] * nums[j + 1])
            dp[(i, j)] = mini
            return mini
        return fn(1, len(nums )- 2)