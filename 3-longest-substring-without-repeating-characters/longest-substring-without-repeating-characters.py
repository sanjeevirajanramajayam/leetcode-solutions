class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        freqMap = {}
        maxLen = 0
        for r in range(len(s)):
            freqMap[s[r]] = freqMap.get(s[r], 0) + 1

            while s[r] in freqMap and freqMap[s[r]] > 1:
                freqMap[s[l]] -= 1
                if freqMap[s[l]] == 0:
                    del freqMap[s[l]]
                l += 1
            maxLen = max(len(freqMap), maxLen)
        return maxLen