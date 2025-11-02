class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        grid = [[-1 for i in range(n)] for j in range(m)]
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for row, col in walls:
            grid[row][col] = 0
        for row, col in guards:
            grid[row][col] = 0
        for row, col in guards:
            for x, y in directions:
                startx = row
                starty = col
                while (startx + x >= 0 and startx + x <= m - 1 ) and (starty + y >= 0 and starty + y <= n - 1):
                    startx += x
                    starty += y
                    if grid[startx][starty] == 0:
                        break
                    grid[startx][starty] = 1
        count = 0
        for i in grid:
            for j in i:
                if j == -1:
                    count += 1
        return count