class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        newNums = sorted([abs(x) for x in nums])
        # print(newNums)
        step = len(nums) // 2
        ans = 0
        for i in range(step):
            ans -= (newNums[i] * newNums[i])
        for i in range(step, len(nums)):
            ans += newNums[i] * newNums[i]
        return ans