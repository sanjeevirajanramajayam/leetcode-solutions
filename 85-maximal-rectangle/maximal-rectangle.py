class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        ROWS = len(matrix)
        COLS = len(matrix[0]) 
        prefixMatrix = [[0 for _ in range(COLS)] for _ in range(ROWS)] 
        for i in range(ROWS):
            for j in range(COLS):
                matrix[i][j] = int(matrix[i][j])
                
        for j in range(COLS):
            count = 0
            for i in range(ROWS):
                count += 1
                if matrix[i][j] == 0:
                    count = 0
                prefixMatrix[i][j] = count
        maxArea = 0
        def maxAreaHist(arr):
            stack = []
            maxArea = 0
            for i in range(len(arr)):
                while stack and arr[stack[-1]] > arr[i]:
                    nse = i
                    element = stack.pop()
                    if stack:
                        pse = stack[-1]
                    else:
                        pse = -1
                    maxArea = max((nse - pse - 1) * arr[element], maxArea) 
                stack.append(i)
            while stack:
                nse = len(arr)
                element = stack.pop()
                if stack:
                    pse = stack[-1]
                else:
                    pse = -1
                maxArea = max((nse - pse - 1) * arr[element], maxArea) 
            return maxArea
        for i in range(len(matrix)):
            maxArea = max(maxArea, maxAreaHist(prefixMatrix[i]))
        return maxArea