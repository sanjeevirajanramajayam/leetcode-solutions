class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ROW = len(grid)
        COL = len(grid[0])
        queue = deque([])
        visited = set()

        freshExist = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                    visited.add((i, j))
                elif grid[i][j] == 1:
                    freshExist = True
        if not freshExist:
            return 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        time = -1
        # print(queue)
        while queue:
            # print(queue)
            size = len(queue)
            for i in range(size):
                row, col = queue.popleft()
                for dr, dc in directions:
                    if row + dr >= 0 and row + dr <= ROW - 1 and col + dc >= 0 and col + dc <= COL - 1:
                        if (row + dr, col + dc) not in visited and grid[row + dr][col + dc] == 1:
                            queue.append((row + dr, col + dc))
                            visited.add((row + dr, col + dc))
            print(queue)
            time += 1
        print(time)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    return -1
        
        return time

