class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS = len(heights)
        COLS = len(heights[0])
        pq = [(0, 0, 0)]
        dist = [[float('inf') for i in range(COLS)] for i in range(ROWS)]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        dist[0][0] = 0
        while pq:
            # print(pq)
            dt, i, j = heapq.heappop(pq)
            if dt > dist[i][j]:
                continue
            for dx, dy in directions:
                nx = i + dx
                ny = j + dy
                if nx >= 0 and nx < ROWS and ny >= 0 and ny < COLS:
                    fh = max(dist[i][j], abs(heights[i][j] - heights[nx][ny]))
                    if fh < dist[nx][ny]:
                        dist[nx][ny] = fh
                        heapq.heappush(pq, (fh, nx, ny))
        return dist[ROWS - 1][COLS - 1]