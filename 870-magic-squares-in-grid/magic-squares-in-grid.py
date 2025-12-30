class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def isMagicSquare(row, col):
            seenSet = set()
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    if grid[i][j] in seenSet:
                        return False
                    if grid[i][j] > 9 or grid[i][j] < 1:
                        return False
                    seenSet.add(grid[i][j])
            diag1 = grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2]
            diag2 = grid[row][col + 2] + grid[row + 1][col + 1] + grid[row + 2][col]

            row1 = grid[row][col] + grid[row][col + 1] + grid[row][col + 2]
            row2 = grid[row + 1][col] + grid[row + 1][col + 1] + grid[row + 1][col + 2]
            row3 = grid[row + 2][col] + grid[row + 2][col + 1] + grid[row + 2][col + 2]

            col1 = grid[row][col] + grid[row + 1][col] + grid[row + 2][col]
            col2 = grid[row][col + 1] + grid[row + 1][col + 1] + grid[row + 2][col + 1]
            col3 = grid[row][col + 2] + grid[row + 1][col + 2] + grid[row + 2][col + 2]

            if diag1 != diag2:
                return False

            if not (row1 == row2 and row2 == row3 and row3 == diag1):
                return False

            if not (col1 == col2 and col2 == col3 and col1 == row1):
                return False

            return True
        count = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                if isMagicSquare(i, j):
                    count += 1
        return count