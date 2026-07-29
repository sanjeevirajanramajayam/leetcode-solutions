class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        newRow = matrix[0][:]
        newRow.sort(reverse=True)
        ans = float('-inf')
        # ans /= max(ans, newRow[i])
        for i in range(len(newRow)):
            ans = max(ans, (i + 1) * newRow[i])
        newRow = matrix[0]
        for k in range(1, len(matrix)):

            for j in range(len(matrix[0])):
                if matrix[k][j] != 0:
                    newRow[j] += matrix[k][j]
                else:
                    newRow[j] = 0
            oldTemp = newRow[:]
            newRow.sort(reverse=True)
            for i in range(len(newRow)):
                ans = max(ans, (i + 1) * newRow[i])
                # print(i + 1, newRow[i])
            # print(newRow)
            newRow = oldTemp[:]
        return ans
        