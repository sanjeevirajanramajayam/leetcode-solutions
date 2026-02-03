class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        queue = deque([])
        visited = set([])

        ROWS = len(board)
        COLS = len(board[0])

        for i in range(COLS):
            if board[0][i] == "O":
                queue.append((0, i))
                visited.add((0, i))
            if board[ROWS - 1][i] == "O":
                queue.append((ROWS - 1, i))
                visited.add((ROWS - 1, i))
        
        for i in range(1, ROWS - 1):
            # print(i, 0)
            if board[i][0] == "O":
                # print("0", i , 0)
                queue.append((i, 0))
                visited.add((i, 0))
            if board[i][COLS - 1] == "O":
                queue.append((i, COLS - 1))
                visited.add((i, COLS - 1))
        
        # print(queue, visited)

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while queue:
            row, col = queue.popleft()

            for dr, dc in directions:
                nrow, ncol = row + dr, col + dc
                if nrow >= 0 and nrow < ROWS and ncol >= 0 and ncol < COLS:
                    if (nrow, ncol) not in visited:
                        if board[nrow][ncol] == "O":
                            queue.append((nrow, ncol))
                            visited.add((nrow, ncol))
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O" and (i, j) not in visited:
                    board[i][j] = "X"
        
            
