class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS = len(mat)
        COLS = len(mat[0])
        queue = deque([])
        visited = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))
        time = 0
        while queue:
            # i, j = queue.popleft()
            qLen = len(queue)
            for i in range(qLen):
                i, j = queue.popleft()
                if mat[i][j] == 1:
                    mat[i][j] = time
                for dx, dy in directions:
                    nx = i + dx
                    ny = j + dy
                    if nx >= 0 and nx < ROWS and ny >= 0 and ny < COLS and (nx, ny) not in visited:
                        # if mat[nx][ny] == 1:
                        queue.append((nx, ny))
                        visited.add((nx, ny))
            time += 1
        return mat
