class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        cnt = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        queue = deque([])

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    queue.append((i, j))
        
        # print(cnt)

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while queue:
            x, y = queue.popleft()
            oldcnt = 0
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                
                if nx >= 0 and nx < ROWS and ny >= 0 and ny < COLS:
                    if grid[nx][ny] == 0:
                        cnt += 1
                else:
                    cnt += 1
            # print(i, j, cnt - oldcnt)
        return cnt

        
