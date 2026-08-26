class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        maxSlope = 0
        for i in range(len(points)):
            slopeMap = defaultdict(int)
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]

                if x1 == x2:
                    slope = float('inf')
                else:
                    slope = (y2 - y1) / (x2 - x1)
                
                slopeMap[slope] += 1
                maxSlope = max(maxSlope, slopeMap[slope])
        return maxSlope + 1
