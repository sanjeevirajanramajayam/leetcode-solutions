class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def lessThanK(k):
            l = 0
            cnt = 0
            ans = 0
            if k < 0:
                return 0
            for r in range(len(nums)):
                if nums[r] == 1:
                    cnt += 1
                while cnt > k:
                    if nums[l] == 1:
                        cnt -= 1
                    l += 1
                ans += (r - l + 1)
            # print(ans)
            return ans
        # print(lessThanK(goal), lessThanK(goal - 1))
        return lessThanK(goal) - lessThanK(goal - 1)