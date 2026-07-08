class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        cnt = 0
        while nums != sorted(nums):
            pairs = []
            minSum = float('inf')
            for i in range(1, len(nums)):
                minSum = min(minSum, nums[i] + nums[i - 1])
            for i in range(1, len(nums)):
                if nums[i] + nums[i - 1] == minSum:
                    pairs.append([i - 1, i])
            pairs.sort(key=lambda x : x[0])
            nums = nums[:pairs[0][0]] + [nums[pairs[0][0]] + nums[pairs[0][1]]] + nums[pairs[0][1] + 1:]
            cnt += 1
        return cnt