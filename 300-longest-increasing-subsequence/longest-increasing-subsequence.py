class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > ans[-1]:
                ans.append(nums[i])
            else:
                l = 0
                r = len(ans) - 1
                temp = 0
                while l <= r:
                    mid = (l + r) // 2
                    if nums[i] > ans[mid]:
                        l = mid + 1
                    else:
                        temp = mid
                        r = mid - 1
                ans[temp] = nums[i]
        return len(ans)