class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def nsplits(k):
            splits = 0
            currSum = 0
            for i in range(len(nums)):
                currSum += nums[i]
                if currSum > k:
                    currSum = nums[i]
                    splits += 1
            return splits + 1
        
        low = max(nums)
        high = sum(nums)
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if nsplits(mid) <= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans