class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def bfs(i, j):
            queue = deque([(i, j)])

            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx >= 0 and nx < ROWS and ny >= 0 and ny < COLS:
                        if grid[nx][ny] == '1' and (nx, ny) not in visited:
                            queue.append((nx, ny))
                            visited.add((nx, ny))
        cnt = 0
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in visited and grid[i][j] == '1':
                    # print(i, j
                    visited.add((i, j))

                    bfs(i, j)
                    cnt += 1
        return cnt
