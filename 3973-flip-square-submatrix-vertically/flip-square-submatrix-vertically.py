class Solution(object):
    def reverseSubmatrix(self, grid, x, y, k):
        """
        :type grid: List[List[int]]
        :type x: int
        :type y: int
        :type k: int
        :rtype: List[List[int]]
        """
        l = x
        r = x + (k - 1)

        while l < r:
            for i in range(y, y + k):
                # print(grid[l][y], grid[r][y])
                grid[l][i], grid[r][i] = grid[r][i], grid[l][i]
                # print(grid[l][y], grid[r][y])
            l += 1
            r -= 1 
        
        return grid
