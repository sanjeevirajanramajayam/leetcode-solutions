class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        minDiff = float('inf')
        ans = 0
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                currSum = nums[l] + nums[r] + nums[i]
                # print(currSum, nums[l], nums[r], nums[i])
                if currSum < target:
                    l += 1
                elif currSum > target:
                    r -= 1
                else:
                    r -= 1
                    l += 1
                if abs(currSum - target) < minDiff:
                    minDiff = abs(currSum - target)
                    ans = currSum
                        # return ans
        return ans
