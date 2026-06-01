class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = deque(cuts)
        cuts.appendleft(0)
        cuts.append(n)
        dp = {}
        def fn(i, j):
            if i > j:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            mini = float('inf')
            for k in range(i, j + 1):
                mini = min(mini, cuts[j + 1] - cuts[i - 1] + fn(i, k - 1) + fn(k + 1, j))
            dp[(i, j)] = mini
            return mini
        return fn(1, len(cuts) - 2)