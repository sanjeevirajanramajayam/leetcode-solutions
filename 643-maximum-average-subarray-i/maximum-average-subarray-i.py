class Solution:
    def findMaxAverage(self, s: List[int], k: int) -> float:
        cnt = 0
        maxCnt = float('-inf')

        for i in range(k):
            cnt += s[i]

        maxCnt = max(maxCnt, cnt / k)
        for i in range(k, len(s)):
            # if s[i - k] in 'aeiou':
            cnt -= s[i - k]
            # if s[i] in 'aeiou':
            cnt += s[i]
            maxCnt = max(maxCnt, cnt / k)
        return maxCnt
