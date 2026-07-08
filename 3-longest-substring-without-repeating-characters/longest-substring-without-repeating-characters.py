class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        size = set()
        maxLen = 0
        for r in range(len(s)):
            while s[r] in size:
                size.remove(s[l])
                l += 1
            size.add(s[r])
            maxLen = max(maxLen, r - l + 1)
        return maxLen
            