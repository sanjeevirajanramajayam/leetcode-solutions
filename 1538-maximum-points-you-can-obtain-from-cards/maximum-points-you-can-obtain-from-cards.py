class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        maxPoints = 0
        points = 0
        for i in range(0, k):
            points += cardPoints[i]
        maxPoints = points
        count = k - 1
        for j in range(len(cardPoints) - 1, len(cardPoints) - k - 1, -1):
            points -= cardPoints[count]
            count -= 1
            points += cardPoints[j]
            maxPoints = max(points, maxPoints)
        return maxPoints