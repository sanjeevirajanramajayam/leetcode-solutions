class Solution:
    def minimumEffortPath(self, h: List[List[int]]) -> int:
        ROWS = len(h) 
        COLS = len(h[0])
        pq = [(0, 0, 0)]
        visited = set([(0, 0)])
        distArray = [[float('inf') for i in range(COLS)] for i in range(ROWS)]
        # print(distArray)
        distArray[0][0] = 0
        directions = [(1, 0), ( 0, 1), (-1, 0), (0, -1)]
        while pq:
            maxDiff, i, j  = heapq.heappop(pq)
            if maxDiff > distArray[i][j]:
                continue
            for dx, dy in directions:
                nx = i + dx
                ny = j + dy
                if nx >= 0 and nx < ROWS and ny >= 0 and ny < COLS:
                    diff = max(distArray[i][j], abs(h[nx][ny] - h[i][j]))
                    if diff < distArray[nx][ny]:
                        distArray[nx][ny] = diff
                        heapq.heappush(pq, (diff, nx, ny))
        return distArray[ROWS - 1][COLS - 1]