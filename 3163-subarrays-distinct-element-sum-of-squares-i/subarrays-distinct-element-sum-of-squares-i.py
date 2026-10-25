class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            temp = set()
            for j in range(i, len(nums)):
                temp.add(nums[j])
                ans += len(temp) * len(temp)
        return ans