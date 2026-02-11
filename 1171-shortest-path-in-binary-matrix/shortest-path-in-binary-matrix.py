class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0] == 1:
            return -1

        ROWS = len(grid)
        COLS = len(grid[0])
        
        pq = [(1, (0, 0))]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (-1, -1), (1, -1)]

        distMat = [[ float('inf') for j in range(COLS)] for i in range(ROWS)]
        distMat[0][0] = 1
        # print(distMat)

        while pq:
            dist, (row, col) = heapq.heappop(pq)
            if dist > distMat[row][col]:
                continue
            for dr, dc in directions:
                nRow, nCol = row + dr, col + dc
                if nRow >= 0 and nRow < ROWS and nCol >= 0 and nCol < COLS:
                    if grid[nRow][nCol] == 0:
                        # print(nRow, nCol, row, col)
                        if dist + 1 < distMat[nRow][nCol]:
                            distMat[nRow][nCol] = dist + 1
                            heapq.heappush(pq, (dist + 1, (nRow, nCol)))
        
        if distMat[ROWS - 1][COLS - 1] == float('inf'):
            return -1
        
        return (distMat[ROWS - 1][COLS - 1])
