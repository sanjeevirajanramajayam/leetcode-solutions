class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col1 = mat[0][0]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    if j == 0:
                        col1 = 0
                    else:
                        mat[0][j] = 0
                    mat[i][0] = 0
        
        for i in range(1, len(mat)):
            for j in range(1, len(mat[0])):
                if mat[0][j] == 0 or mat[i][0] == 0:
                    mat[i][j] = 0
        
        for i in range(len(mat[0]) - 1, -1, -1):
            if mat[0][0] == 0 or mat[0][i] == 0:
                mat[0][i] = 0
        
        for i in range(len(mat)):
            if mat[i][0] == 0 or col1 == 0:
                mat[i][0] = 0
        