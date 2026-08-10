class Solution:
    def characterReplacement(self, nums: str, k: int) -> int:
        maxFreq = float('-inf')
        maxChar = -1
        freqHash = {}
        ans = float('-inf')
        l = 0
        for r in range(len(nums)):
            freqHash[nums[r]] = freqHash.get(nums[r], 0) + 1
            if freqHash[nums[r]] > maxFreq:
                maxFreq = freqHash[nums[r]]
                # maxChar = nums[r]
            # print(freqHash)
            # print(maxFreq)
            while maxFreq + k < (r - l + 1):
                freqHash[nums[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans