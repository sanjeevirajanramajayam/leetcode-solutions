class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        
        def fn(sum):
            splits = 1
            currSum = 0
            for i in range(len(nums)):
                currSum += nums[i]
                if currSum > sum:
                    currSum = nums[i]
                    splits += 1
            return splits

        ans = -1
        while low <= high:
            mid = (low + high) // 2
            # print(mid, fn(mid))
            if fn(mid) <= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans