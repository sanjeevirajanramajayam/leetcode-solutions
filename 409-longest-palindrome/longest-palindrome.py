class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = {}
        for i in range(len(s)):
            hashmap[s[i]] = hashmap.get(s[i], 0) + 1
        evenSum = 0
        picked = False
        maxOddSum = 0
        # print(hashmap)
        for i in hashmap:
            if hashmap[i] % 2 == 0:
                evenSum += hashmap[i]
            else:
                evenSum += hashmap[i] - 1
                picked = True
        if picked:
            return evenSum + 1
        return evenSum 