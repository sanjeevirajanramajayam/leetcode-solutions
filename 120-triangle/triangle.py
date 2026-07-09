class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ROWS = len(triangle)
        @cache
        def fn(i ,j):
            if i == ROWS - 1:
                return triangle[i][j]
            
            left = triangle[i][j] + fn(i + 1, j)
            right = triangle[i][j] + fn(i + 1, j + 1)

            return min(left, right)
        return fn(0, 0)