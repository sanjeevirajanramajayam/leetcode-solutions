class Solution(object):
    def separateSquares(self, squares):
        """
        :type squares: List[List[int]]
        :rtype: float
        """

        def onY(givenY):
            upArea = 0
            downArea = 0
            for i in range(len(squares)):
                x, y, l = squares[i]
                if y >= givenY:
                    upArea += l * l
                elif y + l <= givenY:
                    downArea += l * l
                else:
                    w = givenY - y
                    downArea += w * l
                    upArea += (l * l) - (w * l)
            return upArea - downArea

        low = min([y for (x, y, _) in squares])
        high = max([y + l for (x, y, l) in (squares)])

        episilon = 10 ** (-6)

        while high - low >= episilon:
            mid = (high + low) / 2.0
            diff = onY(mid)
            if diff > 0:
                low = mid
            else:
                high = mid 
        return (low + high) / 2