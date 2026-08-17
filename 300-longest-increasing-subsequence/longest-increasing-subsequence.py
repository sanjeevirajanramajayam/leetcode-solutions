class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []
        for i in range(len(nums)):
            if not lis or nums[i] > lis[-1]:
                lis.append(nums[i])
            else:
                l = 0
                r = len(lis) - 1
                ans = -1
                while l <= r:
                    mid = (l + r) // 2
                    if lis[mid] >= nums[i]:
                        ans = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                lis[ans] = nums[i]
        return len(lis)