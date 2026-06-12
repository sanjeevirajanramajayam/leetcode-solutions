class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[(row + col * n) for row in range(n)] for col in range(n)]
        # print(matrix)
        c = 1
        top = 0
        bottom = n - 1
        left = 0
        right = n - 1
        while top <= bottom and left <= right:
            # top
            for i in range(left, right + 1):
                matrix[top][i] = c
                c += 1
            top += 1

            # right
            for i in range(top, bottom + 1):
                matrix[i][right] = c
                c += 1
            right -= 1

            # bottom
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = c
                c += 1
            bottom -= 1

            # left

            for i in range(bottom, top - 1, -1):
                matrix[i][left] = c
                c += 1
            left += 1
        return matrix

