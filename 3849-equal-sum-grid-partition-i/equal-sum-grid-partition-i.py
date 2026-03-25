class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        rowsSum = [0 for i in range(len(grid))]
        colsSum = [0 for j in range(len(grid[0]))]
        total = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                rowsSum[i] += grid[i][j]
                colsSum[j] += grid[i][j]
                total += grid[i][j]
        rowTotal = 0
        for row in rowsSum:
            if rowTotal == total - rowTotal:
                return True
            rowTotal += row
    
        colTotal = 0
        for col in colsSum:
            if colTotal == total - colTotal:
                return True
            colTotal += col
        
        return False