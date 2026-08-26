class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        class DSU:
            def __init__(self, V):
                self.V = V
                self.parent = [i for i in range(V)]
                # print(self.parent)
                self.size = [1 for i in range(V)]
            
            def find_parent(self, node):
                if node == self.parent[node]:
                    return node
                self.parent[node] = self.find_parent(self.parent[node])
                return self.parent[node]
            
            def union(self, u, v):
                u = self.find_parent(u)
                v = self.find_parent(v)

                if u == v:
                    return

                if self.size[u] > self.size[v]:
                    self.size[u] += self.size[v]
                    self.parent[v] = u
                elif self.size[u] < self.size[v]:
                    self.size[v] += self.size[u]
                    self.parent[u] = v
                else:
                    self.size[v] += self.size[u]
                    self.parent[u] = v
        ROWS = len(grid)
        COLS = len(grid[0])

        dsu = DSU(ROWS * COLS)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                        nx = i + dx
                        ny = j + dy

                        if nx >= 0 and nx < ROWS and ny >= 0 and ny < COLS:
                            if grid[nx][ny] == 1:
                                coord1 = nx * COLS + ny
                                coord2 = i * COLS + j
                                dsu.union(coord1, coord2)
        # print(dsu.parent)
        maxi = float('-inf')
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    vset = set()
                    for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                        nx = i + dx
                        ny = j + dy

                        if nx >= 0 and nx < ROWS and ny >= 0 and ny < COLS:
                            if grid[nx][ny] == 1:
                                vset.add(dsu.find_parent(nx * COLS + ny))
                    ans = 0
                    # print(vset)
                    # print(dsu.size)
                    for parent in vset:
                        ans += dsu.size[parent]
                    maxi = max(maxi, ans + 1)
        if maxi == float('-inf'):
            return ROWS * COLS
        return maxi