class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + cuts + [n]
        # print(cuts)
        cuts.sort()
        @cache
        def fn(i, j):
            if i > j:
                return 0
            
            mini = float('inf')
            for k in range(i, j + 1):
                # print(i ,j)
                cost = (cuts[j + 1] - cuts[i - 1]) + fn(i, k - 1) + fn(k + 1, j)
                mini = min(cost, mini)
            return mini
        return fn(1, len(cuts) - 2)