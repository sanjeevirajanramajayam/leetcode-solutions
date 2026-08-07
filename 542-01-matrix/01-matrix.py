class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque([])
        ROWS = len(mat)
        COLS = len(mat[0])
        visited = set()
        for i in range(ROWS):
            for j in range(COLS):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))
                    visited.add((i, j))
        while queue:
            # print(queue)
            x, y, dist = queue.popleft()
            if mat[x][y] == 1:
                mat[x][y] = dist

            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx = x + dx
                ny = y + dy
                if nx >= 0 and nx < ROWS and ny >= 0 and ny < COLS and (nx, ny) not in visited:
                    if mat[nx][ny] == 1:
                        queue.append((nx, ny, dist + 1))
                        visited.add((nx, ny))
        return mat

