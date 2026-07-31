class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        l = 0
        hash = {}
        pairs = 0
        ans = l
        for r in range(len(nums)):
            hash[nums[r]] = hash.get(nums[r], 0) + 1
            pairs += (hash[nums[r]] - 1)
            # print(pairs, r, nums[r], hash)
            while pairs >= k:
                # print(pairs)
                hash[nums[l]] = hash.get(nums[l], 0) - 1
                pairs -= hash[nums[l]]
                l += 1
            # print(l)
            ans += l
        return ans