class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        hash = {}
        maxFreq = float('-inf')
        ans = float('-inf')
        l = 0
        for r in range(len(s)):
            hash[s[r]] = hash.get(s[r], 0) + 1
            maxFreq = max(maxFreq, hash[s[r]])
            
            if maxFreq + k < (r - l + 1):
                # print(l)
                hash[s[l]] = hash.get(s[l], 0) - 1
                l += 1
            
            ans = max(ans, r - l + 1)
        return ans