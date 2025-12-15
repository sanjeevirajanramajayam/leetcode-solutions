class Solution(object):
    def getDescentPeriods(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        count = 1
        l = 0
        prevVal = prices[l]
        for r in range(1, len(prices)):
            if prices[r] == prevVal - 1:
                prevVal = prices[r]
                count += (r - l + 1)
            else:
                l = r
                prevVal = prices[l]
                count += 1
        return count