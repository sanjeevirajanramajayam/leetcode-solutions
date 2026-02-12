class Solution(object):
    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLen = 0
        for i in range(len(s)):
            hashMap = {}
            for j in range(i, len(s)):
                hashMap[s[j]] = hashMap.get(s[j], 0) + 1
                # print(hashMap)
                if len(set(hashMap.values())) == 1:
                    maxLen = max(maxLen, sum(hashMap.values()))
        return maxLen