class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = set([])
        ROWS = len(grid)
        COLS = len(grid[0])
        # distinctIslands = set()
        count = 0
        
        def bfs(row, col):
            queue = deque([(row, col)])
            visited.add((row, col))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            # pathList = [(0, 0)]
            # base = (row, col)
            while queue:
                cRow, cCol = queue.popleft()
                for dRow, dCol in directions:
                    nRow, nCol = cRow + dRow, cCol + dCol
                    if nRow >= 0 and nRow < ROWS and nCol >= 0 and nCol < COLS:
                        if (nRow, nCol) not in visited and grid[nRow][nCol] == "1":
                            queue.append((nRow, nCol))
                            visited.add((nRow, nCol))
                            # print(nRow, nCol)
                            # pathList.append((nRow - base[0], nCol - base[1]))
            # print(pathList)
            # distinctIslands.add(tuple(pathList))                 
                
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == "1":
                    bfs(i, j)
                    count += 1
        
        return count