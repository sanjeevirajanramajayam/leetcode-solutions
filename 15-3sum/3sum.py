class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            target = -nums[i]
            while l < r:
                currSum = nums[l] + nums[r]
                if currSum == target:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif currSum > target:
                    r -= 1
                else:
                    l += 1
                # print(l > i + 1 , nums[l], nums[l - 1])
                while l > i + 1 and l < len(nums) and nums[l] == nums[l - 1]:
                    l += 1
                
                while r < len(nums) - 1 and r >= 0 and  nums[r] == nums[r + 1]:
                    r -= 1
        return ans