class Solution(object):
    def numberOfSubmatrices(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        xMat = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        yMat = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                xleft = 0
                yleft = 0
                if j - 1 >= 0:
                    xleft = xMat[i][j - 1]
                    yleft = yMat[i][j - 1]

                xtop = 0
                ytop = 0
                if i - 1 >= 0:
                    xtop = xMat[i - 1][j]
                    ytop = yMat[i - 1][j]

                xdiag = 0
                ydiag = 0
                if i - 1 >= 0 and j - 1 >= 0:
                    xdiag = xMat[i - 1][j - 1]
                    ydiag = yMat[i - 1][j - 1]

                if grid[i][j] == 'X':
                    xMat[i][j] = xtop + xleft - xdiag + 1
                    yMat[i][j] = ytop + yleft - ydiag
                elif grid[i][j] == 'Y':
                    xMat[i][j] = xtop + xleft - xdiag
                    yMat[i][j] = ytop + yleft - ydiag + 1
                else:
                    xMat[i][j] = xtop + xleft - xdiag
                    yMat[i][j] = ytop + yleft - ydiag

                if xMat[i][j] >= 1 and xMat[i][j] == yMat[i][j]:
                    count += 1

        return count