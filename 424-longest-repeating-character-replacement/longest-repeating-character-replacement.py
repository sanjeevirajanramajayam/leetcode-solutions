class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = 0
        hashmap = {}
        maxFreq = 0
        maxLen = 0
        for r in range(len(s)):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
            maxFreq = max(maxFreq, hashmap[s[r]])

            while (r - l + 1) - maxFreq > k:
                if s[l] in hashmap:
                    hashmap[s[l]] -= 1
                l += 1

            if (r - l + 1 - maxFreq <= k):
                maxLen = max(r - l + 1, maxLen)
        return maxLen

