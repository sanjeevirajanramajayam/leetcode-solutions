class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def fn(maxSum):
            splits = 1
            currSum = 0
            for i in nums:
                currSum += i
                # print(currSum)
                if currSum > maxSum:
                    currSum = i
                    splits += 1
            # print(splits)
            return splits
        fn(17)
        low = max(nums)
        high = sum(nums)
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if fn(mid) <= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans