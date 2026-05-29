class Solution:
    def minElement(self, nums: List[int]) -> int:
        mini = float('inf')
        for i in range(len(nums)):
            val = sum(map(int, list(str(nums[i]))))
            mini = min(mini, val)
            nums[i] = val
        return mini
