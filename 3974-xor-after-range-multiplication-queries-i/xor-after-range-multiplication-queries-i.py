class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for l, r, step, mul in queries:
            for i in range(l, r + 1, step):
                nums[i] = (nums[i] * mul) % (10**9 + 7)
        ans = 0
        for i in nums:
            ans ^= i
        return ans