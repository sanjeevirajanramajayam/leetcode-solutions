class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        pq = [(0, 0, 0)]
        ROWS = len(heights)
        COLS = len(heights[0])
        dist = [[float('inf') for _ in range(COLS)] for _ in range(ROWS)]
        dist[0][0] = 0

        while pq:
            dt, row, col = heapq.heappop(pq)

            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx = row + dx
                ny = col + dy
                if nx >= 0 and nx < ROWS and ny >= 0 and ny < COLS:
                    newDiff = max(dt, abs(heights[nx][ny] - heights[row][col]))
                    if newDiff < dist[nx][ny]:
                        dist[nx][ny] = newDiff
                        heapq.heappush(pq, (newDiff, nx, ny))
            # print(pq)
        return dist[ROWS - 1][COLS - 1]