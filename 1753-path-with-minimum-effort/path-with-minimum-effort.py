class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """

        pq = ([(0, (0, 0))])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ROWS = len(heights)
        COLS = len(heights[0])
        distMatrix = [[float('inf') for i in range(COLS)] for j in range(ROWS)]
        # print(distMatrix)
        distMatrix[0][0] = 0
        
        while pq:
            maxDiff, (row, col) = heapq.heappop(pq)
            if maxDiff > distMatrix[row][col]:
                continue
            for nrow, ccol in directions:
                cRow, cCol = row + nrow, col + ccol
                if cRow >= 0 and cRow < ROWS and cCol >= 0 and cCol < COLS:
                    diff = max(maxDiff, abs(heights[cRow][cCol] - heights[row][col]))
                    if diff < distMatrix[cRow][cCol]:
                        distMatrix[cRow][cCol] = diff
                        heapq.heappush(pq, (diff, (cRow, cCol)))
            # print(pq)
        # print(distMatrix)
        return distMatrix[-1][-1]    