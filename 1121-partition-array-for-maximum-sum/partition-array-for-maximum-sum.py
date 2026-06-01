class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = {}
        def fn(ind):
            if ind == len(arr):
                return 0
            length = 0
            maxVal = float('-inf')
            maxi = float('-inf')
            if ind in dp:
                return dp[ind]
            for l in range(ind, min(len(arr), ind + k)):
                maxVal = max(maxVal, arr[l])
                length += 1
                maxi = max(maxi, length * maxVal + fn(l + 1))
            dp[ind] = maxi
            return maxi
        return fn(0)