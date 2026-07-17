class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix[0]) - 1

        while i < len(matrix) and j >= 0:
            print(matrix[i][j])
            if matrix[i][j] < target:
                i += 1
            elif matrix[i][j] > target: 
                j -= 1
            else:
                return True
        return False
        