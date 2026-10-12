class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        low = 0
        high = ROWS * COLS 
        high -= 1

        while low <= high:
            mid = (low + high) // 2
            r = mid // COLS 
            c = mid % COLS 
            if matrix[r][c] == target:
                return True 
            elif matrix[r][c] > target:
                high=mid - 1
            else:
                low = mid + 1
            # print(r, c) 
        return False