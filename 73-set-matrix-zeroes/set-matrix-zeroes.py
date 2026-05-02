class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        colSet = set()
        rowSet = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    colSet.add(j)
                    rowSet.add(i)

        for i in rowSet:
            for j in range(len(matrix[0])):
                # print(i, j)
                matrix[i][j] = 0

        for i in range(len(matrix)):
            for j in colSet:
                matrix[i][j] = 0
         