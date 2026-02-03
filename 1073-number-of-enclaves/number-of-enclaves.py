class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set([])

        def dfs(row, col):
            for dr, dc in directions:
                nr, nc = row + dr, col +  dc
                if nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS:
                    if (nr, nc) not in visited:
                        if grid[nr][nc] == 1:
                            visited.add((nr, nc))
                            dfs(nr, nc)

        for i in range(COLS):
            if grid[0][i] == 1:
                dfs(0, i)
                visited.add((0, i))
            if grid[ROWS - 1][i] == 1:
                dfs(ROWS - 1, i)
                visited.add((ROWS - 1, i))
        
        for i in range(1, ROWS - 1):
            if grid[i][0] == 1:
                dfs(i, 0)
                visited.add((i, 0))
            if grid[i][COLS - 1] == 1:
                dfs(i, COLS - 1)
                visited.add((i, COLS - 1))

        count = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i, j) not in visited:
                    count += 1
                    
        return count




        