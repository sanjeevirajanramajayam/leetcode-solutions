class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        ans = [0] * len(matrix)
        for i in range(len(matrix)):
            count = 0
            for j in matrix[i]:
                if j == 1:
                    count += 1
            ans[i] = count
        return ans