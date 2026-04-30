class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        grid = [[0] * m for i in range(n)]
        queue = deque([])
        ROWS = n
        COLS = m
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        sources.sort(key=lambda x: -x[2])
        for r, c, col in sources:
            grid[r][c] = col
            queue.append((r, c, col))
        # visited = set()
        while queue:
            r, c, col = queue.popleft()
            for dx, dy in directions:
                nx, ny = r + dx, c + dy
                if nx >= 0 and nx < ROWS and ny >= 0 and ny < COLS and grid[nx][ny] == 0:
                    queue.append((nx, ny, col))
                    # visited.add((nx, ny))
                    grid[nx][ny] = col

            # print(queue)
        return grid