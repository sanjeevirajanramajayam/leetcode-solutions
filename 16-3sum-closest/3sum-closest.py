class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float('inf')
        ans = 0
        i = 0
        while i < len(nums) - 1:
            # while  and nums[i] == nums[i - 1]:

            l = i + 1
            r = len(nums) - 1                
            # currSum = nums[i] + nums[l] + nums[r]

            while l < r:            
                currSum = nums[i] + nums[l] + nums[r]
                absDiff = abs(target - currSum)
                if absDiff < diff:
                    ans = currSum
                    diff = absDiff

                if currSum > target:
                    r -= 1
                elif currSum < target:
                    l += 1
                else:
                    r -= 1
                    l += 1
            i += 1
                


        return ans