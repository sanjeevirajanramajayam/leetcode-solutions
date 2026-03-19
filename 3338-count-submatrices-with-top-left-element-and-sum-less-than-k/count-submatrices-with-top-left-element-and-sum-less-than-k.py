class Solution(object):
    def countSubmatrices(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        prefixMat = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                left = 0
                if j - 1 >= 0:
                    left = prefixMat[i][j - 1]

                top = 0
                if i - 1 >= 0:
                    top = prefixMat[i - 1][j]

                diag = 0
                if i - 1 >= 0 and j - 1 >= 0:
                    diag = prefixMat[i - 1][j - 1]
                
                prefixMat[i][j] = left + top - diag + grid[i][j]

                if prefixMat[i][j] <= k:
                    # print(i, j)
                    count += 1
        return count