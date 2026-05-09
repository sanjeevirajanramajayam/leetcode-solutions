class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        def fn(r, c, m, n):
            sr, sc = (r, c)
            last = grid[sr][sc]
            first = -1
            # print(sr, sc)
            while sr != m - 1:
                # print("start", sr, sc, last, grid[sr][sc])
                sr += 1
                # print(last)
                temp = grid[sr][sc]
                grid[sr][sc] = last
                last = temp
                # print(sr, sc, grid[sr][sc])
            while sc != n - 1:
                sc += 1
                temp = grid[sr][sc]
                grid[sr][sc] = last
                last = temp
                # print(sr, sc, grid[sr][sc])
            while sr > r:
                sr -= 1
                temp = grid[sr][sc]
                grid[sr][sc] = last
                last = temp
                # print(sr, sc, grid[sr][sc])
            while sc > c:
                temp = grid[sr][sc]
                sc -= 1
                temp = grid[sr][sc]
                grid[sr][sc] = last
                last = temp
                # print(sr, sc, grid[sr][sc])
        # fn(1, 1, m - 1, n - 1)
# Process layer by layer
# FIXED LOGIC APART FROM FN:
        num_layers = min(m, n) // 2
        for i in range(num_layers):
            # 1. Calculate layer-specific dimensions
            # layer_h and layer_w are the number of elements in the current layer's sides
            layer_h = m - 2 * i
            layer_w = n - 2 * i
            
            # 2. Calculate the perimeter for THIS layer
            perimeter = 2 * layer_h + 2 * layer_w - 4
            
            # 3. Use modulo to find the effective rotations needed
            net_k = k % perimeter
            
            # 4. Define the boundaries for your fn function
            # Your fn expects the "m" and "n" arguments to be the bottom and right indices
            bottom_boundary = m - i
            right_boundary = n - i
            
            for _ in range(net_k):
                fn(i, i, bottom_boundary, right_boundary)
                
        return grid