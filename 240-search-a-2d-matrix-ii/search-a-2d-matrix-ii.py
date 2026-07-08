class Solution:
    def searchMatrix(self, m: List[List[int]], x: int) -> bool:
        ROWS = len(m)
        COLS = len(m[0])

        r = 0
        c = COLS - 1

        while r >= 0 and r < ROWS and c >= 0 and c < COLS:
            if m[r][c] == x:
                return True
            if m[r][c] > x:
                c -= 1
            else:
                r += 1
        return False