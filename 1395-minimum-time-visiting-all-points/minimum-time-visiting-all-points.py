class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        prevPoints = points[0]
        time = 0
        for i in range(1, len(points)):
            time += max(abs(prevPoints[0] - points[i][0]), abs(prevPoints[1] - points[i][1]))
            prevPoints = points[i]
        return time