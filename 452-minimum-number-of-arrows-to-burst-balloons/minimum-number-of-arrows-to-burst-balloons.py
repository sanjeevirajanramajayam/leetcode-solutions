class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: (x[1]))
        ans = 0
        last_end = 0
        for start, end in points:
            if ans == 0 or start > last_end:
                last_end = end
                ans += 1
        return ans
        
                