class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = 0
        maxLen = 0
        maxFreq = 0
        charHash = {}
        for r in range(len(s)):
            charHash[s[r]] = charHash.get(s[r], 0) + 1
            maxFreq = max(charHash[s[r]], maxFreq)
            while (r - l + 1) - maxFreq > k:
                charHash[s[l]] -= 1
                l += 1
            if (r - l + 1) - maxFreq <= k:
                maxLen = max(maxLen, (r - l + 1))
        return maxLen