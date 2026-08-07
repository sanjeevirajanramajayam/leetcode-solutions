class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def lessThanK(k):
            if k < 0:
                return 0
            l = 0
            oneCnt = 0
            ans = 0
            for r in range(len(nums)): 
                if nums[r] % 2 == 1:
                    oneCnt += 1
                while oneCnt > k:
                    if nums[l] % 2 == 1:
                        oneCnt -= 1
                    l += 1
                ans += (r - l) + 1
                # print(ans, r, l)
            return ans
        return lessThanK(k) - lessThanK(k - 1)