class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(1, 0), (0, 1), (1, 1), (-1, 1), (1, -1), (-1, -1), (-1, 0), (0, -1)]
        if (grid[0][0] == 1):
            return -1
        queue = deque([(0, 0, 1)])
        visited = set([(0, 0)])
        while queue:
            # print(queue)
            x, y, d = queue.popleft()
            if x == ROWS - 1 and y == COLS - 1:
                return d
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if nx >= 0 and nx < ROWS and ny >= 0 and ny < COLS and (nx, ny) not in visited:
                    if grid[nx][ny] == 0:
                        queue.append((nx, ny, d + 1))
                        visited.add((nx, ny))
        return -1