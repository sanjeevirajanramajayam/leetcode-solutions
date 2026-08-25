class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        
        def dfs(i, j):
            visited.add((i, j))

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx = i + dx
                ny = j + dy

                if nx >= 0 and nx < ROWS and ny >= 0 and ny < COLS and grid[nx][ny] == "1":
                    if (nx, ny) not in visited:
                        dfs(nx, ny)
        cnt = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i, j) not in visited:
                    # print(i, j)
                    dfs(i, j)
                    cnt += 1
        return cnt
        