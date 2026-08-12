class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        row = matrix[0]
        maxArea = 0
        minW = float('inf')
        temp = row[:]
        row.sort(reverse=True)
        # print(row)
        for i in range(len(row)):
            if row[i] == 1:
                minW = min(minW, row[i])
                maxArea = max(maxArea, minW * (i + 1))
        row = temp
        for k in range(1, len(matrix)):
            minW = float('inf')
            # row = matrix[k]
            for i in range(len(matrix[k])):
                if matrix[k][i] == 1:
                    row[i] += 1
                else:
                    row[i] = 0
            # print(row)
            
            temp = row[:]
            row.sort(reverse=True)
            # print(row)
            for i in range(len(row)):
                if row[i] != 0:
                    minW = min(minW, row[i])
                    maxArea = max(maxArea, minW * (i + 1))
                    print(minW, i + 1)
            row = temp
        return maxArea