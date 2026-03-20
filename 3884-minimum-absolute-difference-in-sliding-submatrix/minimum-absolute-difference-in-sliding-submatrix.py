class Solution(object):
    def minAbsDiff(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        ROWS = len(grid)
        COLS = len(grid[0])
        ans = [[0 for i in range(COLS - k + 1)] for i in range(ROWS - k + 1)]
        # print(ans)
        for i in range(ROWS - k + 1):
            for j in range(COLS - k + 1):
                subMatArr = []
                for u in range(i, i + k):
                    for v in range(j, j + k):
                        # print(u, v, grid[u][v])
                        subMatArr.append(grid[u][v])
                subMatArr.sort()
                # print(subMatArr)
                minDiff = float('inf')
                for w in range(1, len(subMatArr)):
                    if subMatArr[w] != subMatArr[w - 1]:
                        minDiff = min(minDiff, abs(subMatArr[w] - subMatArr[w - 1]))
                # print(minDiff)
                if minDiff == float('inf'):
                    minDiff = 0
                ans[i][j] = minDiff

        return ans