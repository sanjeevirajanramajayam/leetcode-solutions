class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)
        leftSum = 0
        maxPoints = 0
        for i in range(k):
            leftSum += cardPoints[i]
        maxPoints = max(maxPoints, leftSum)
        tempK = k
        for i in range(n - 1, n - k - 1, -1):
            leftSum -= cardPoints[tempK - 1]
            tempK -= 1
            leftSum += cardPoints[i]
            maxPoints = max(maxPoints, leftSum)
        return maxPoints
