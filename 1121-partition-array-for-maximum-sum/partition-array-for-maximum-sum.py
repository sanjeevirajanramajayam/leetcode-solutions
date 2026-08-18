class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        @cache
        def fn(i):
            if i == len(arr):
                return 0
            ans = float('-inf')
            maxi = float('-inf')
            for j in range(i, min(i + k, len(arr))):
                maxi = max(maxi, arr[j])
                ans = max(maxi * (j - i + 1) + fn(j + 1), ans)
            return ans 
        return fn(0)
