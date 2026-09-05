class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        island1 = set()
        island2 = set()

        ROWS = len(grid)
        COLS = len(grid[0])

        def bfs(i, j):
            visited = set()
            visited.add((i, j))
            queue = deque([(i, j)])
        
            while queue:
                # print(queue)
                row, col = queue.popleft()
                for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nrow = row + dx
                    ncol = col + dy
                    if nrow >= 0 and nrow < ROWS and ncol >= 0 and ncol < COLS and grid[nrow][ncol] == 1:
                        if (nrow, ncol) not in visited:
                            queue.append((nrow, ncol))
                            visited.add((nrow, ncol))
            return visited
                    

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    if not island1:
                        island1 = bfs(i, j)
                    elif (i, j) not in island1:
                        island2 = bfs(i, j)
                        break
            if island2:
                break
        
        queue = deque(list(island1))
        visited = set(island1)
        # print(queue, visited)
        dist = 0
        while queue:
            qLen = len(queue)

            for _ in range(qLen):
                row, col = queue.popleft()

                for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nrow = row + dx
                    ncol = col + dy

                    if 0 <= nrow < ROWS and 0 <= ncol < COLS:

                        if (nrow, ncol) in island2:
                            return dist

                        if (nrow, ncol) not in visited:
                            visited.add((nrow, ncol))
                            queue.append((nrow, ncol))

            dist += 1