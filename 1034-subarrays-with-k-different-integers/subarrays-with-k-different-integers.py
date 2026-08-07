class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def lessThanK(k):
            if k < 0:
                return 0
            cnt = 0
            l = 0
            hash = {}
            for r in range(len(nums)):
                hash[nums[r]] = hash.get(nums[r], 0) + 1
                while len(hash) > k:
                    hash[nums[l]] = hash.get(nums[l], 0) - 1
                    if hash[nums[l]] == 0:
                        del hash[nums[l]]
                    l+=1
                cnt += (r - l) + 1
            return cnt
        return lessThanK(k) - lessThanK(k - 1)