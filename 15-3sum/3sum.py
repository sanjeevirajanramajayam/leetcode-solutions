class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        prevI = float('-inf')
        for i in range(len(nums)):
            if prevI != float('-inf'):
                if nums[i] == prevI:
                    continue
                else:
                    prevI = nums[i]
            else:
                prevI = nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                zeroSum = nums[i] + nums[j] + nums[k]
                if zeroSum > 0:
                    k -= 1
                elif zeroSum < 0:
                    j += 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    prevJ = nums[j]
                    while j < len(nums) and nums[j] == prevJ:
                        j += 1
                    prevK = nums[k]
                    while k >= 0 and nums[k] == prevK:
                        k -= 1
        return ans