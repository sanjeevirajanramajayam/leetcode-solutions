class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        
        ROWS = len(mat)
        COLS = len(mat[0])

        ans = [[0 for _ in range(COLS)] for _ in range(ROWS)]

        queue = deque([])
        visited = set([])

        for i in range(ROWS):
            for j in range(COLS):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))
                    visited.add((i, j))

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        distance = 0
        
        while queue:
            distance += 1
            size = len(queue)
            for i in range(size):
                cRow, cCol, dist = queue.popleft()
                ans[cRow][cCol] = dist
                
                found = False
                for dr, dc in directions:
                    uRow, uCol = cRow + dr, cCol + dc
                    if uRow >= 0 and uRow < ROWS and uCol >= 0 and uCol < COLS:
                        if (uRow, uCol) not in visited:
                            queue.append((uRow, uCol, dist + 1))
                            visited.add((uRow, uCol))

        return ans