class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)        
        visited = set()
        queue = deque([])
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j, 0))
                    visited.add((i, j))
        ROWS = len(grid)
        COLS = len(grid[0])
        minDist = [[0 for i in range(n)] for i in range(n)]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while queue:
            i, j, dist = queue.popleft()
            minDist[i][j] = dist
            for dx, dy in directions:
                nx = i + dx
                ny = j + dy
                if nx >= 0 and nx < ROWS and ny >= 0 and ny < COLS and (nx, ny) not in visited:
                    queue.append((nx, ny, dist + 1))
                    visited.add((nx, ny))
        print(minDist)
        # return 0

        pq = [(-minDist[0][0], 0, 0)]
        dist = [[float('-inf') for i in range(n)] for i in range(n)]
        dist[0][0] = minDist[0][0]
        while pq:
            dt, i, j = heapq.heappop(pq)
            dt = -dt
            for dx, dy in directions:
                nx = i + dx
                ny = j + dy
                if nx >= 0 and nx < ROWS and ny >= 0 and ny < COLS:
                    if min(dist[i][j], minDist[nx][ny]) > dist[nx][ny]:
                        dist[nx][ny] = min(dist[i][j], minDist[nx][ny])
                        heapq.heappush(pq, (-dist[nx][ny] , nx, ny))
        # print(dist)

        return dist[ROWS - 1][COLS - 1]