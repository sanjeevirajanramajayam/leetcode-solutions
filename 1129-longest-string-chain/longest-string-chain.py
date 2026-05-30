class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = [1 for i in range(len(words))]
        words.sort(key=len)
        def compare(s1, s2):
            # print(s1, s2)
            if len(s1) + 1 != len(s2):
                return False
            i = 0
            j = 0
            while j < len(s2):
                if i < len(s1) and s1[i] == s2[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
            
            if i == len(s1) and j == len(s2):
                return True
            return False

        for i in range(len(words)):
            for j in range(0, i):
                if compare(words[j], words[i]) and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1

        return max(dp)