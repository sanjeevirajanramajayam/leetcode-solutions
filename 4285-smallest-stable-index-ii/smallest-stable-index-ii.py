class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        maxArray = [float('-inf')] * len(nums)
        minArray = [float('inf')] * len(nums)
        maxArray[0] = nums[0]
        minArray[len(nums) - 1] = nums[len(nums) - 1]
        for i in range(1, len(nums)):
            if nums[i] > maxArray[i - 1]:
                maxArray[i] = nums[i]
            else:
                maxArray[i] = maxArray[i - 1]
        # print(maxArray)
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < minArray[i + 1]:
                minArray[i] = nums[i]
            else:
                minArray[i] = minArray[i + 1]
        # print(minArray)
        ans = float('inf')
        for i in range(len(nums)):
            if maxArray[i] - minArray[i] <= k:
                ans = min(ans, i)
        if ans == float('inf'):
            return -1 
        return ans