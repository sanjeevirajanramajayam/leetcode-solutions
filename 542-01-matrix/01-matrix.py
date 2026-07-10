class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS = len(mat) 
        COLS = len(mat[0]) 
        queue = deque([])
        visited = set()
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))
        time = 1
        while queue:
            # print(queue)
            qlen = len(queue)
            for _ in range(qlen):
                i, j = queue.popleft()
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    # print(visited)
                    if nx >= 0 and nx < ROWS and ny >= 0 and ny < COLS:
                        if (nx, ny) not in visited:
                            if mat[nx][ny] == 1:
                                mat[nx][ny] = time
                                queue.append((nx, ny))
                                visited.add((nx, ny))
            time += 1
        return mat