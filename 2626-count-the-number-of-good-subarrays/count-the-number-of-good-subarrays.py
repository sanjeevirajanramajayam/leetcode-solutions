class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        l = 0
        pairs = 0
        hash = {}
        ans = 0
        for r in range(len(nums)):
            hash[nums[r]] = hash.get(nums[r], 0) + 1
            pairs += (hash[nums[r]] - 1)
            # print(nums[l:r+1], pairs, hash)
            while pairs >= k:
                hash[nums[l]] = hash.get(nums[l], 0) - 1
                pairs -= hash[nums[l]]
                l += 1
            
            ans += l
        return ans