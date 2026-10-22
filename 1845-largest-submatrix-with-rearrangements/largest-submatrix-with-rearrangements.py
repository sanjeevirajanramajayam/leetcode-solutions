class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        maxArea = float('-inf')
        dst = matrix[0]

        tempdst = sorted(dst)[::-1]
        # print(tempdst)
        mini = float('inf')
        for j in range(COLS):
            # mini = min(mini, tempdst[j])
            maxArea = max(maxArea, tempdst[j] * (j + 1))

        for i in range(1, ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    dst[j] = 0 
                else:
                    dst[j] += 1 
            # print(dst)
            tempdst = sorted(dst)[::-1]
            # print(tempdst)
            mini = float('inf')
            for j in range(COLS):
                # mini = min(mini, tempdst[j])
                maxArea = max(maxArea, tempdst[j] * (j + 1))
        return maxArea