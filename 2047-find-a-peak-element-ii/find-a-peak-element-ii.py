class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        ROWS = len(mat)
        COLS = len(mat[0])
        low = 1
        high = COLS - 2

        maxIdx = -1
        maxElement = float('-inf')

        if COLS == 1:
            maxIdx = -1
            maxElement = float('-inf')

            for i in range(ROWS):
                if maxElement < mat[i][COLS - 1]:
                    maxElement = mat[i][COLS - 1]
                    maxIdx = i
            
            return [maxIdx, COLS - 1]

        for i in range(ROWS):
            if maxElement < mat[i][0]:
                maxElement = mat[i][0]
                maxIdx = i
        
        if maxElement > mat[maxIdx][1]:
            return [maxIdx, 0]

        maxIdx = -1
        maxElement = float('-inf')

        for i in range(ROWS):
            if maxElement < mat[i][COLS - 1]:
                maxElement = mat[i][COLS - 1]
                maxIdx = i

        if maxElement > mat[maxIdx][COLS - 2]:
            return [maxIdx, COLS - 1]
        
        while low <= high:
            mid = (low + high) // 2
            print(low, high, mid)

            maxIdx = -1
            maxElement = float('-inf')

            for i in range(ROWS):
                if maxElement < mat[i][mid]:
                    maxElement = mat[i][mid]
                    maxIdx = i
            # print(maxElement, mat[maxIdx][mid + 1], mat[maxIdx][mid - 1])
            if maxElement > mat[maxIdx][mid + 1] and maxElement > mat[maxIdx][mid - 1]:
                return [maxIdx, mid]

            if maxElement <= mat[maxIdx][mid + 1]:
                low = mid + 1
            else:
                high = mid - 1