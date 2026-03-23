class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefixMatrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                diag = 0
                up = 0
                left = 0

                if i - 1 >= 0 and j - 1 >= 0:
                    diag += self.prefixMatrix[i - 1][j - 1]

                if i - 1 >= 0:
                    up += self.prefixMatrix[i - 1][j]

                if j - 1 >= 0:
                    left += self.prefixMatrix[i][j - 1]
                
                self.prefixMatrix[i][j] = left + up - diag + matrix[i][j]
            

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        if row1 - 1 >= 0:
            total += self.prefixMatrix[row2][col2] - self.prefixMatrix[row1 - 1][col2]
        else:
            total = self.prefixMatrix[row2][col2]
        
        if col1 - 1 >= 0:
            total -= self.prefixMatrix[row2][col1 - 1]
        
        if row1 - 1 >= 0 and col1 - 1 >= 0:
            total += self.prefixMatrix[row1 - 1][col1 - 1]
        
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)