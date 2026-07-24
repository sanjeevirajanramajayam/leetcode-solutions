class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newWord = ""
        l = 0
        r = 0
        for i in range(min(len(word1), len(word2))):
            newWord += word1[l]
            newWord += word2[r]
            l += 1
            r += 1
        while l < len(word1):
            newWord += word1[l]
            l += 1
        while r < len(word2):
            newWord += word2[r]
            r += 1
        return newWord