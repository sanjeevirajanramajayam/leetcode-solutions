class Solution:
    def largestDivisibleSubset(self, words: List[int]) -> List[int]:
        dp = [1 for i in range(len(words))]
        path = [i for i in range(len(words))]
        words.sort()
        for i in range(len(words)):
            for j in range(0, i):
                if words[i] % words[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    path[i] = j
        index = dp.index(max(dp))
        ans = []
        while index != path[index]:
            ans.append(words[index])
            index = path[index]
        ans.append(words[index])
        return ans[::-1]