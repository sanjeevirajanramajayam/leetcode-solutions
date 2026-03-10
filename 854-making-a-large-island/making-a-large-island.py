class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        class DSU:
            def __init__(self, n):
                self.parent = [i for i in range(n)]
                self.size = [1 for i in range(n)]
            
            def get_parent(self, node):
                if node == self.parent[node]:
                    return node
                self.parent[node] = self.get_parent(self.parent[node])
                return self.parent[node]
            

            
            def union(self, x, y):
                uX = self.get_parent(x)
                uY = self.get_parent(y)

                if uX == uY:
                    return
                
                if self.size[uX] > self.size[uY]:
                    self.parent[uY] = uX
                    self.size[uX] += self.size[uY]
                else:
                    self.parent[uX] = uY
                    self.size[uY] += self.size[uX]
                
        
        ROWS = len(grid)
        COLS = len(grid[0])
        dsu = DSU((ROWS * COLS) + 1)
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    for dx, dy in directions:
                        nx, ny = i + dx, j + dy
                        if nx >= 0 and nx < ROWS and ny >= 0 and ny < COLS:
                            if grid[nx][ny] == 1:
                                coord1 = nx * ROWS + 1 + ny
                                coord2 = i * ROWS + 1 + j
                                dsu.union(coord1, coord2)
        maxSize = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    components = set()
                    for dx, dy in directions:
                        nx, ny = i + dx, j + dy
                        if nx >= 0 and nx < ROWS and ny >= 0 and ny < COLS:
                            if grid[nx][ny] == 1:
                                coord1 = nx * ROWS + 1 + ny
                                components.add(dsu.get_parent(coord1))
                    size = 1
                    # print(i, j)
                    # print(components)
                    for comp in components:
                        size += dsu.size[comp]
                    maxSize = max(maxSize, size)
        for i in range((ROWS * COLS) + 1):
            maxSize = max(maxSize, dsu.size[i])
        return maxSize