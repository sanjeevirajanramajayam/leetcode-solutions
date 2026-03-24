class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ROWS = len(maze)
        COLS = len(maze[0])
        visited = set([(entrance[0], entrance[1])])
        minTime = float('inf')
        def bfs(row, col, time):
            nonlocal minTime
            queue = deque([(row, col, time)])

            while queue:
                row, col, time = queue.popleft()
                if (row == 0 or col == 0 or row == ROWS - 1 or col == COLS - 1) and ((row, col) !=(entrance[0], entrance[1])):
                    minTime = min(time, minTime)
                # print(row, col, queue)
                for dx, dy in directions:
                    nx, ny = row + dx, col + dy
                    if nx >= 0 and nx < ROWS and ny >= 0 and ny < COLS:
                        if maze[nx][ny] == '.' and (nx, ny) not in visited:
                            queue.append((nx, ny, time + 1))
                            visited.add((nx, ny))
        bfs(entrance[0], entrance[1], 0)
        return -1 if minTime == float('inf') else minTime